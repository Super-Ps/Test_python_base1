#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/9/30

#from socket import  *

import socket

'''
cs = socket()   # 创建客户套接字
comm_loop:      # 通讯循环
    cs.sendto()/cs.recvfrom()   # 对话(发送/接收)
cs.close()   

'''

c_ip = ("127.0.0.1", 8001)

BUFSIZE = 20
c_udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while 1:
    input_msg = input(">>>>>>>>>").strip()
    if not input_msg:continue
    # 发送 输入的内容且需要设置编码，传递目标IP地址
    c_udp.sendto((input_msg),c_ip)
    back_s_conn,back_s_ip = c_udp.recvfrom(BUFSIZE)
    print("客户端接收服务端发送信息是%s,ip是"%back_s_conn.decode("utf-8"),back_s_ip)
    print("接收服务端信息类型是：",type(back_s_conn))
