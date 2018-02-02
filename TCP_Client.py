# -*- coding:utf-8 -*-
from getpass import getpass
import socket
import time
import pickle
import os

class MyClient(object):
    def __init__(self,HOST,PORT,user_info_file=None):
        if user_info_file == None:
            self.user_info_file = 'C:/Documents and Settings/Administrator/user_info.pkl'
        self._socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self._socket.connect((HOST,PORT))
        self.get_user_info()
        #建立user_info的副本,最后比对user_info是否发生变化
        self.user_info_copy = self.user_info[:]

    def send(self,message):
        self._socket.send(message)

    def sendall(self,message):
        self._socket.sendall(message)

    def recv(self):
        return self._socket.recv(4096)

    def get_user_info(self):
        f = open(self.user_info_file,'r')
        #self.user_info is a list  [{n1:p1},{n2:p2},....]
        self.user_info = pickle.load(f)
        f.close()

    def add_user_info(self,name,password):
        self.user_info.append({name:password})
    
    def ch_passwd(self,name,passwd):
        for i in range(len(self.user_info)):
            if self.user_info[i].has_key(name):
                self.user_info[i] = {name:passwd}
                break

    def has_user(self,username):
        HAVE = False
        for user in self.user_info:
            #user is a dict    [n:p]
            if user.has_key(username):
                HAVE = user
                break
        return HAVE
    
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
##        print self.user_info_copy != self.user_info
##        print self.user_info_copy
##        print self.user_info
        if self.user_info_copy != self.user_info:
            print 'overwrite user_info file successful'
            f = open(self.user_info_file,'w')
            pickle.dump(self.user_info,f)
            f.close()
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
    HOST = 'localhost'
    PORT = 9999
    mc = MyClient(HOST,PORT)
    print 'Welcome to TCP Client'
    login = False
    while not login:
        username = raw_input('Input your username>')
        user = mc.has_user(username)
        if user:
            for i in range(3,0,-1):
                print "you have %d time(s) to input password"%i
                passwd = getpass('Input your password>')
                if passwd == str(user[username]):
                    print "login success, %s" % username
                    login = True
                    break
            if not login:
                mc.close()
                os.sys.exit(0)
        if not login:
            print 'wrong name,pleace input again!'
    while True:
        screen_print()
        ch = raw_input('choose one of the command>')
        if ch == 'exit':
            break
        elif ch == 'terminal':
            while True:
                cmd = raw_input('<%s>%s$'% (ch,username))
                if cmd == 'exit':
                    break
                if not cmd:continue
                mc.use_command(ch,cmd)
        elif ch == 'adduser':
            print "#please do not set password as exit ,it's conflict with system command.#"
            while True:
                add_user = raw_input('<%s>Pleace input username:'%ch)
                if not add_user:continue
                if add_user == 'exit':
                    break
                if mc.has_user(add_user):
                    print "The user '%s' is already exist,please change another name"%add_user
                    continue
                while True:
                    add_passwd1 = getpass('<%s>Pleace input you password:'%ch)
                    if add_passwd1 == 'exit':
                        print 'can not set password as exit'
                        continue
                    add_passwd2 = getpass('<%s>Pleace input you password again:'%ch)
                    if add_passwd1 == add_passwd2:
                        mc.add_user_info(add_user,add_passwd1)
                        print "add user '%s' successful"%add_user
                        break
                    else:
                        print '两次输入的密码不一致'.decode('utf-8').encode('gb2312')
                        continue
        elif ch == 'resetpasswd':
            print "#please do not set password as exit ,it's conflict with system command.#"
            _continue = True
            while _continue:
                pw = getpass('<%s>Pleace input you old password:'%ch)
                if pw == 'exit':
                    break
                if pw == str(user[username]):
                    while True:
                        passwd1 = getpass('<%s>Pleace input you new password:'%ch)
                        passwd2 = getpass('<%s>Pleace input you new password again:'%ch)
                        if passwd1 == passwd2:
                            mc.ch_passwd(username,passwd1)
                            print 'reset password successful'
                            _continue = False
                            break
                        else:
                            print '两次输入的密码不一致'.decode('utf-8').encode('gb2312')
                            continue
                else:
                    print 'wrong password,please try again!'
        elif ch == 'getfile':
            while True:
                pass
        elif ch == 'sendfile':
            pass
        else:
            print "no function '%s' ,please iuput again!"%ch


    mc.close()
##HOST = 'localhost'
##PORT = 9999
##
##s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
##s.connect((HOST,PORT))
##    
##s.close()


