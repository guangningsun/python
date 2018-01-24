# -*- coding:utf-8 -*-
#!/usr/bin/env python

import socket
import sys

HOST ='127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = raw_input('请输入>')
    if not data:
        break
    tcpCliSock.send("%s\r\n" % data)
    resp = tcpCliSock.recv(BUFSIZ)
    if not resp:
        break
    print resp
tcpCliSock.close()
