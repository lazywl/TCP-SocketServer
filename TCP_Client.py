# -*- coding:utf-8 -*-
import socket
import time
import pickle
import os

class MyClient(object):
    def __init__(self,HOST,PORT):
        self._socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self._socket.connect((HOST,PORT))

    def send(self,message):
        self._socket.send(message)

    def sendall(self,message):
        self._socket.sendall(message)

    def recv(self):
        return self._socket.recv(4096)
    
    def getfile(self,file_name):
        pass

    def sendfile(self,file_name):
        pass

    def addSeparator(self,ch,message):
        return '%s#%s' % (ch,message)
    
    def use_command(self,ch,cmd):
        self.send(self.addSeparator(ch,cmd))
        data = self.recv()
        try:
            data = data.decode('utf-8').encode('gb2312')
        except UnicodeDecodeError as e:
            pass
        print data

    def close(self):
        self._socket.close()

def screen_print():
    print '##########################################################'
    print "#you can type the follow cmd to use it's function        #"
    print '#         getfile       ? get <file_name> ?              #'
    print '#         sendfile      ? send <file_name> ?             #'
    print '#         terminal      ? like the linux terminal ?      #'
    print '#         adduser       ? add <[username,passwd]> ?      #'
    print '#         resetpasswd   ? reset <passwd>  ?              #'
    print '##########################################################'
##HOST = 'localhost'
##PORT = 9999
##mc = MyClient(HOST,PORT)
##screen_print()


if __name__ == '__main__':
    print 'Welcome to TCP Client'
    login = False
    while not login:
        username = raw_input('Input your username>')
        with open('C:/Documents and Settings/Administrator/user_info.pkl') as f:
            user_info = pickle.load(f)
            for user in user_info:
                if user.has_key(username):
                    for i in range(3,0,-1):
                        print "you have %d time(s) to input password"%i
                        passwd = raw_input('Input your password>')
                        if passwd == str(user[username]):
                            print "login success, %s" % username
                            login = True
                            break
                    if not login:os.sys.exit(0)
                if login:break
        if not login:
            print 'wrong name,pleace input again!'
    HOST = 'localhost'
    PORT = 9999
    mc = MyClient(HOST,PORT)
    while True:
        screen_print()
        ch = raw_input('choose one of the command>')
        if ch == 'exit':
            break
        if ch == 'terminal':
            while True:
                cmd = raw_input('%s$'%username)
                if cmd == 'exit':
                    break
                mc.use_command(ch,cmd)



    mc.close()
##HOST = 'localhost'
##PORT = 9999
##
##s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
##s.connect((HOST,PORT))
##    
##s.close()


