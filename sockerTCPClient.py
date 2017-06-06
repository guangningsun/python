# -*- coding:utf-8 -*-
#!/usr/bin/env python

import socket
from SocketServer import (TCPServer as TCP, StreamRequestHandler as SRH)

HOST ='127.0.0.1'
SPORT = 21567
DPORT = 21568
BUFSIZ = 1024
SADDR = (HOST, SPORT)
DADDR = (HOST, DPORT)

#class MyRequestHandler(SRH):
#    def handle(self):
#        print 'connected from ',self.client_address
#        data = raw_input('response>>')
#        self.wfile.write("[%s] %s " % (ctime(), data)


while True:
    tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpCliSock.connect(SADDR)
    data = raw_input('请输入>')
    if not data:
        break
    tcpCliSock.send("%s\r\n" % data)
    resp = tcpCliSock.recv(BUFSIZ)
    if not resp:
        break
    print resp
tcpCliSock.close()
