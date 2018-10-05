#-*- coding:utf-8 -*-
import socket   #소켓 모듈을 임포트한다.
HOST = '127.0.0.1'      #로컬호스트를 적는다.

PORT = 55555        #포트를 지정한다
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #소켓을 생성한다. SOCK_STREAM:tcp방식
print('서버 실행합니다...')
s.bind((HOST, PORT))    #주소와 소켓을 결합한다.
s.listen(1)     #연결 요청을 청취 하나의 요청만 받는다고 1을 지정
conn, addr = s.accept()     #클라이언트로부터 온 연결 요청(connect)을 수락하고 연결 소켓을 생성
print('Connected by', addr)
while 1:
    data = conn.recv(1024)      #클라이언트에 데이터를 수신(1024바이트 수만큼 수신하겠다)
    if not data: break
    conn.send(data +b'  :from server')  #클라이언트로 데이터 송신
conn.close()    #서버 종료, null값반환

