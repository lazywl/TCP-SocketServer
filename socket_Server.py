# -*- coding:utf-8 -*-
import socket
HOST = ''
PORT = 3333
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(2)
conn,addr = s.accept()

#-----------------

print 'Got connection from:',addr
while 1:
    data = conn.recv(4096)
    if not data:break
    #print 'Receive data from Client:',data
    conn.sendall(data)

conn.close()
