# -*- coding:utf-8 -*-
import SocketServer
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
                    result = "你输入的命令'%s'无法执行" % self.data
                #返回执行结果
                self.request.sendall(result)   

if __name__ == "__main__":
    HOST,PORT = 'localhost',9999

    #开启Server并绑定地址和端口号
    server = SocketServer.ThreadingTCPServer((HOST,PORT),MyTCPHandler)

    #激活服务器，服务器将会一直运行直到按Ctrl-C
    server.serve_forever()
