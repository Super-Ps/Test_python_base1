#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/9/19

import socket

ADDR=('127.0.0.1',8009)

host_name=socket.gethostname()
print(host_name)

host_namex=socket.gethostbyname_ex('zhengxiaojiao')
print(host_namex)

cilent = socket.socket()

cilent.connect(ADDR)  # 连接客户端

while True:
    data = input('>>> ')
    if not data: break
    else:
        print("已经连接")
cilent.close()


#
# 注意点:
# 1）TCP发送数据时，已建立好TCP连接，所以不需要指定地址。UDP是面向无连接的，每次发送要指定是发给谁。
# 2）服务端与客户端不能直接发送列表，元组，字典。需要字符串化repr(data)。









import socket

HOST = '192.168.1.101'
PORT = 2222

def send_data(data):

    try:
        sock_clt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock_clt.connect((HOST, PORT))
        sock_clt.send(data)
    finally:
        sock_clt.close()


while True:
    send_data('16进制'

'''

import socket
HOST='10.0.0.245'
PORT=50007
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)      #定义socket类型，网络通信，TCP
s.connect((HOST,PORT))       #要连接的IP与端口
while 1:
       cmd=raw_input("Please input cmd:")       #与人交互，输入命令
       s.sendall(cmd)      #把命令发送给对端
       data=s.recv(1024)     #把接收的数据定义为变量
        print data         #输出变量
s.close()   #关闭连接
'''