import socketserver
import threading

HOST = '127.0.0.1'
PORT = 8888
lock = threading.Lock()     #syncronized 동기화 진행하는 스레드 생성,

class UserManager:      #사용자관리 및 채팅 메세지 전송을 담당하는 클래스

    def __init__(self):
        self.users = {}     #사용자의 등록 정보를 담을 사전 {사용자 이름: (소켓, ip주소).....}

    def addUser(self, username, conn, addr):    #사용자ID를 self.users에 추가하는 함수
        if username in self.users:     #이미 등록된 사용자라면
            conn.send('이미 등록된 사용자입니다.\n'.encode())
            return None

        #새로운 사용자를 등록함
        lock.acquire()  #스레드 동기화를 막기위한 락
        self.users[username] = (conn, addr)
        lock.release()     #업데이트 후 락 해제

        self.sendMessageToAll('[%s]님이 입장했습니다.' % username)
        print('+++ 대화 참여자 수 [%d]' % len(self.users))

        return username

    def removeUser(self, username):     #사용자를 제거하는 함수
        if username not in self.users:
            return

        lock.acquire()
        del self.users[username]
        lock.release()

        self.sendMessageToAll('[%s]님이 퇴장했습니다.' % username)
        print('---대화 참여자 수 [%d]' % len(self.users))

    def messageHandler(self, username, msg):    #전송한 msg를 처리하는 부분
        if msg[0] != '/':      #보낸 메세지의 첫문자가 '/'가 아니면
            self.sendMessageToAll('[%s] %s' % (username, msg))
            return

        if msg.strip() == '/quit':       #보낸 메세지가 'quit'이면, strip(): 맨마지막 줄바꿈문자 제거
            self.removeUser(username)
            return - 1

    def sendMessageToAll(self, msg):
        for conn, addr in self.users.values():
            conn.send(msg.encode())

class MyTcpHandler(socketserver.BaseRequestHandler):
    user = UserManager()

    def handle(self):   #클라이언트가 접속시 클라이언트 주소 출력
        print('[%s] 연결됨' % self.client_address[0])

        try:
            username = self.registerUsername()
            msg = self.request.recv(1024)
            while msg:
                print(msg.decode())
                if self.user.messageHandler(username, msg.decode()) == -1:
                    self.request.close()
                    break
                msg = self.request.recv(1024)

        except Exception as e:
            print(e)

        print('[%s] 접속 종료' % self.client_address[0])
        self.user.removeUser(username)

    def registerUsername(self):
        while True:
            self.request.send('로그인ID:'.encode())
            username = self.request.recv(1024)
            username = username.decode().strip()
            if self.user.addUser(username, self.request, self.client_address):
                return username


class MultiChatServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def runServer():      #무한루프
    # print('Chat Server Start!!(end:ctrl+c)')

    try:
        chat_server = MultiChatServer((HOST, PORT), MyTcpHandler)
        chat_server.serve_forever()    #클라이언트의 갯수에 상관없이 threading을 포함한 서버 소켓을 구동시킴
    except KeyboardInterrupt:
        print('Chat Server end!!')
        chat_server.shutdown()
        chat_server.server_close()

if __name__ == "__main__":
    runServer()



