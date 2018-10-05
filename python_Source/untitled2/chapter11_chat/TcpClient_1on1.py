#-*- coding:utf-8 -*-
import socket   #소켓모듈을 임포트 한다.
HOST = '127.0.0.1' #서버에 접속할 주소를 지정
PORT = 9999        #서버에 접속할 포트를 지정한다.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #소켓을 생성한다.
#socket.AF_INET 에서 ip4를 사용하는 것을 지정.
#socket.SOCK_STREAM에서 TCP 를 사용하는 것을 지정.
s.connect((HOST, PORT))#연결을 설정한다.
while True:
    msg = input('송신>')
    s.send(msg.encode(encoding='utf-8', errors='strict')) #서버로 데이터를 송신한다.
    if msg =='exit':
        break
    data = s.recv(1024) #서버로 부터 데이터를 수신한다.
    print('수신>'+data.decode())
s.close()