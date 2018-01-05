#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/9/28

from socket import *
'''
cs = socket() # 创建客户套接字
cs.connect() # 尝试连接服务器
comm_loop: # 通讯循环
cs.send()/cs.recv() # 对话（发送／接收）
cs.close() # 关闭客户套接字

'''
def Tcp_client():

    C_HOST = "127.0.0.1"
    C_PORT = 8022

    C_ADDR = (C_HOST,C_PORT)
    tcp_client = socket(AF_INET, SOCK_STREAM)

    tcp_client.connect(C_ADDR)

    while 1:
        msg_data = input(">>>>>>>").strip()
        if not msg_data:
            continue
        tcp_client.send(msg_data.encode("utf-8  "))
        # 服务器由于某种原因退出，导致recv()函数失败

        c_respons_data = tcp_client.recv(1024).decode("utf-8  ")
        # if not c_respons_data:
        #     break
        print(c_respons_data)
        tcp_client.close()

Tcp_client()

# if __name__ == "__main__ ":
#     Tcp_client()