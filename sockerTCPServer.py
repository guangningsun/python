# -*- coding:utf-8 -*-
#!/usr/bin/env python

from SocketServer import (TCPServer as TCP, StreamRequestHandler as SRH)
import socket
from time import ctime

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)
class MyRequestHandler(SRH):
    def handle(self):
        print 'connected from ',self.client_address
        self.data = self.request.recv(1024).strip()
        if self.data:
            print self.data
        data_input = raw_input('>>>>>')
        self.wfile.write("[%s] %s" % (ctime(), data_input))

tcpServ = TCP(ADDR, MyRequestHandler)
print 'waiting for connection...'
tcpServ.serve_forever()
