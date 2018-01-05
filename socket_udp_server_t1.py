#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/9/28

#from socket import *
import socket

'''
1 ss = socket()   #创建一个服务器的套接字
2 ss.bind()       #绑定服务器套接字
3 inf_loop:       #服务器无限循环
4     cs = ss.recvfrom()/ss.sendto() # 对话(接收与发送)
5 ss.close()                         # 关闭服务器套接字
'''

s_ip= ("127.0.0.1",8001)
BUFSIZE = 40
s_udp =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s_udp.bind(s_ip)

#不需要接收 直接循环发送

while 1:
    print("开启upd服务.....")
    #接收客户端对象，IP，设置接收大小

    c_conn,c_ip = s_udp.recvfrom(BUFSIZE)
    print("服务器接收客户端的信息是：%s,%s,%s"%(c_conn.decode(),c_ip,type(c_conn)))

    #向客户端发送信息
    s_udp.sendto(c_conn,c_ip)

