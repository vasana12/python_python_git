import socket
from threading import Thread

HOST = '127.0.0.1'
PORT = 8888

def recvMsg(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(data.decode())    #문자열로 변환
        except:
            pass

def runChat():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        t = Thread(target=recvMsg, args=(sock,))    #소켓객체 파라미터전달, 소켓객체로 데이터 송신/수신
        t.daemon = True     #메인스레드가 종료되면 데몬스레도 종료되게 설정
        t.start()

        while True:
            msg = input()
            if msg == '/quit':
                sock.send(msg.encode())
                break

            sock.send(msg.encode())

if __name__ == "__main__":
    runChat()