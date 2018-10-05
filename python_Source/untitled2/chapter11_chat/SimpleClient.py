#-*-coding: utf-8 -*-
import socket #소켓모듈을 임포트한다.
HOST = '127.0.0.1' #서버에 접속할 주소를 저장
PORT = 55555 #서버에 접속할 포트를 지정한다.
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #소켓을 생성한다.
s.connect((HOST,PORT)) #서버에 연결한다. 이때 서버는accept()메소드가 호출된다.
s.send('Hello world'.encode(encoding='utf-8',errors='strict')) #서버로 데이터를 송신한다.
data=s.recv(1024) #서버로 부터 데이터를 수신한다.
s.close() #소켓프로그램을 종료한다.
print(data) #서버로부터 수신한 데이터를 출력한다.