#-*- coding:utf-8 -*-
from socket import *
from time import ctime

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('waiting for message ...')
    data, ADDR = udpSerSock.recvfrom(BUFSIZ)

    udpSerSock.sendto(str(data).encode('UTF-8', 'strict'), ADDR)
    print('... received from and returned to :', ADDR)

udpSerSock.close()