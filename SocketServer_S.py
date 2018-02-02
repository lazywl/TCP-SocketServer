# -*- coding:utf-8 -*-
import SocketServer
import time
import os

class MyTCPHandler(SocketServer.BaseRequestHandler):
    '''
    构造自己的RequestHandler类，
    '''
    def handle(self):
        print "{} wrote:".format(self.client_address[0])
        
        while True:
            print 'ok'
            self.data = self.request.recv(4096)
            if not self.data:break
            ch,file_name = self.data.split()
            if ch == 'get':
                if os.path.exists(file_name):
                    f = open(file_name)
                    data = f.read()
                    f.close()
                    self.request.sendall(data)
##                    time.sleep(1)
                    self.request.send('done!')
                else:
                    self.request.send('None')
            else:
                get = False
                f = open(file_name,'w')
                while True:
                    data = self.request.recv(4096)
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
                    os.remove(file_name)

#在服务器段使用ls ,dir 等命令
##        while 1:
##            #self.request 就是socket的connect对象
##            self.data = self.request.recv(4096)
##            if not self.data:break
##            print 'will run this in server:',self.data
##            cmd = os.popen(self.data)
##            result = cmd.read()
##            if result == '':
##                result = "你输入的命令'%s'无法执行" % self.data
##            #返回执行结果
##            self.request.sendall(result)
##            
##            #将接收到的数据返回客户端
##            #self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST,PORT = 'localhost',9999

    #开启Server并绑定地址和端口号
    server = SocketServer.ThreadingTCPServer((HOST,PORT),MyTCPHandler)

    #激活服务器，服务器将会一直运行直到按Ctrl-C
    server.serve_forever()
