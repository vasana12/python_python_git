#-*-coding: utf-8 -*-
from socket import *

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('>')
    if not data:
        break
    udpCliSock.sendto(str(data).encode(encoding='utf-8', errors = 'strict'), ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print (data,ADDR)

udpCliSock.close()