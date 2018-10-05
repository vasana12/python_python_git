#-*- coding:utf-8 -*-
import socket
import threading

bind_ip = '127.0.0.1'
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET에서 ip4를 사용하는 것을 지정, socket.SOCK_STREAM에서 TCP를 사용하는 것을 지정.

server.bind((bind_ip, bind_port))
#자신의 IP주소와 port를 설정한다.
#상대방의 IP 주소와 port 를 설정하는 경우 connect 를 사용한다고 생각해도 좋다.

server.listen(5)
#연결의 최대 저장 수를 설정한다.
print('[*]Listening on % s: %d'%(bind_ip,bind_port))

def handle_client(client_socket):
    bufsize = 1024
    while True:
        request = client_socket.recv(bufsize)
        client_socket.send(request)
        if request == 'exit':
            break
    client_socket.close()

while True:
    client, addr = server.accept()
    #bind 된 소켓에서 새로운 소켓과 연결된 주소를 반환한다.
    print('[*] Accepted connection from : %s:%d' %(addr[0], addr[1]))

    client_handler = threading.Thread(target=handle_client, args= (client,))
    #threading 을 사용하여 스레드를 생성한다.
    #멀티 코어에 대응시키고 싶은 경우는 multiporcessing 를 사용하면 된다.
    #target은 호출 함수 (객체)를 지정하고 args 는 그 인수를 지정 하고 있다.

    client_handler.start()
    #처리를 시작한다.