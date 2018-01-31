# -*- coding:utf-8 -*-
import socket
import time
HOST = 'localhost'
PORT = 3333

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
while 1:
    s.sendall('Hello,World')
    time.sleep(1)
    data = s.recv(1240)
    print 'Received data from Server:',data
s.close()

