# -*- coding:utf-8 -*-
import socket
import time
HOST = 'localhost'
PORT = 9999

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
'''
while 1:
    s.sendall('Hello,World')
    time.sleep(1)
    data = s.recv(1240)
    print 'Received data from Server:',data
    '''
while 1:
    INPUT = raw_input('Input:')
    if INPUT == 'exit':
        exit()
    s.sendall(INPUT)
    data = s.recv(4096)
    print 'Received data from Server:',data

s.close()

