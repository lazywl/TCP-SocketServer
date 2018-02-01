# -*- coding:utf-8 -*-
import socket
import time
import os
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
    output = 'Received data from Server:' + os.linesep + data
    #print type(output)

    try:
        output = output.decode('utf-8').encode('gb2312')
    except UnicodeDecodeError as e:
        pass
    
    print output

s.close()

