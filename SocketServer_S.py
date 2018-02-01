# -*- coding:utf-8 -*-
import SocketServer
import os

class MyTCPHandler(SocketServer.BaseRequestHandler):
    '''
    构造自己的RequestHandler类，
    '''
    def handle(self):
        print "{} wrote:".format(self.client_address[0])
        while 1:
            #self.request 就是socket的connect对象
            self.data = self.request.recv(4096)
            if not self.data:break
            print 'will run this in server:',self.data
            cmd = os.popen(self.data)
            result = cmd.read()
            print result
            #返回执行结果
            self.request.sendall(result)
            
            #将接收到的数据返回客户端
            #self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST,PORT = 'localhost',9999

    #开启Server并绑定地址和端口号
    server = SocketServer.ThreadingTCPServer((HOST,PORT),MyTCPHandler)

    #激活服务器，服务器将会一直运行直到按Ctrl-C
    server.serve_forever()
