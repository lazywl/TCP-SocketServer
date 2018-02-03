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

while True:
    INPUT = raw_input('Input:')
    s.send(INPUT)
    ch,file_name = INPUT.split()
    if ch == 'get':
        get = False
        f = open('E:/%s'%file_name,'wb')
        while True:
            data = s.recv(4096)
            if data == 'None':
                print 'no file name %s'%file_name
                f.close()
                break
            if data != 'done!':
                f.write(data)
            else:
                f.close()
                get = True
                break
        if get:
            print 'get file %s successful'%file_name
        else:
            os.remove('E:/%s'%file_name)
    else:
        send = False
        if os.path.exists('E:/%s'%file_name):
            f = open('E:/%s'%file_name,'rb')
            while True:
                data = f.read(4096)
                if not data:
                    break
                s.send(data)
            f.close()
            time.sleep(0.5)
            s.send('done!')
            send = True
        else:
            s.send('None')
        if send:
            print 'send file %s successful'%file_name

#在服务器段使用ls ,dir 等命令
##while 1:
##    INPUT = raw_input('Input:')
##    if INPUT == 'exit':
##        exit()
##    s.sendall(INPUT)
##    data = s.recv(4096)
##    output = 'Received data from Server:' + os.linesep + data
##    #print type(output)
##
##    try:
##        output = output.decode('utf-8').encode('gb2312')
##    except UnicodeDecodeError as e:
##        pass
##    
##    print output

s.close()

