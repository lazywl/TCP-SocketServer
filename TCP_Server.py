# -*- coding:utf-8 -*-
import SocketServer
import time
import os

class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        print 'get connection from {}'.format(self.client_address)
        while True:
            self.data = self.request.recv(4096)
            if not self.data:break
            ch,self.data = self.data.split('#')
            if ch == 'terminal':
                #self.request 就是socket的connect对象
                cmd = os.popen(self.data)
                result = cmd.read()
                if result == '':
                    result = "Error:你输入的命令'%s'无法执行" % self.data
                #返回执行结果
                self.request.sendall(result)
                time.sleep(0.5)
                self.request.send('done')
            elif ch == 'get':
                send = False
                if os.path.exists(self.data):
                    f = open(self.data,'rb')
                    while True:
                        data = f.read(4096)
                        if not data:
                            break
                        self.request.send(data)
                    f.close()
                    time.sleep(0.5)
                    self.request.send('done!')
                    send = True
                else:
                    self.request.send('None')
                if send:
                    print 'send file %s successful'%self.data
            else:
                get = False
                self.data = os.path.split(self.data)[1]
                f = open(self.data,'wb')
                while True:
                    data = self.request.recv(4096)
                    if data == 'None':
                        print 'no file name %s'%self.data
                        f.close()
                        break
                    if data != 'done!':
                        f.write(data)
                    else:
                        f.close()
                        get = True
                        break
                if get:
                    print 'get file %s successful'%self.data
                else:
                    os.remove(self.data)

if __name__ == "__main__":
    HOST,PORT = 'localhost',9999

    #开启Server并绑定地址和端口号
    server = SocketServer.ThreadingTCPServer((HOST,PORT),MyTCPHandler)
  
    #激活服务器，服务器将会一直运行直到按Ctrl-C
    server.serve_forever()
