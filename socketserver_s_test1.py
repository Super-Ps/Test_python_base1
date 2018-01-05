#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/9/30

import socketserver
import socket




class MyServer(socketserver.BaseRequestHandler):
    def setup(self):
        pass

    def handle(self):
        #print(self.request, self.client_address, self.server)

        # 1.self.request 就是客户端对象，被封装了，下面转换1个变量来标示客户端
        conn = self.request
        # 2.客户端连接过来，发送消息....
        # 此处注意转型成bytes 编码
        conn.send(("hello!.").encode())
        # 定义循环条件为真
        flag = True
        #进入循环
        while flag:
            # 循环接收客户端信息，并解码
            # 此处注意转型成bytes 解码
            data = conn.recv(1024).decode()
            print( data )
            # 判断客户端 输入exit 循环条件就为假
            if data =='exit':
                flag = False
            # 每接收到后发送信息。并编码
            conn.send(('sb').encode())
        conn.close()

    def finish(self):
        pass

if __name__ == '__main__':


    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8818), MyServer)
    server.serve_forever()




