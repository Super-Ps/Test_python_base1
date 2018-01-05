#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/9/28

from socket import *

'''
ss = socket() # 创建服务器套接字
ss.bind() # 把地址绑定到套接字上
ss.listen() # 监听连接
inf_loop: # 服务器无限循环
cs = ss.accept() # 接受客户的连接
comm_loop: # 通讯循环
cs.recv()/cs.send() # 对话（接收与发送）
cs.close() # 关闭客户套接字
ss.close() # 关闭服务器套接字（可选）

'''
def TcpServer():
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    # 定义IP和端口
    HOST="127.0.0.1"
    PORT=8022

    ADDR=(HOST,PORT)
    #绑定
    tcp_socket.bind(ADDR)
    #监听
    tcp_socket.listen(10)

    while 1:
        print("等待接收.........")
        # 无线循环等待接收，返回客户端连接，地址
        client_conn, client_addr = tcp_socket.accept()
        # re =sock.accept()  分解写法
        # client_conn =re[0]
        # client_addr = re[1]

        print('接受到自来%s的请求' %client_addr)
        while 1:
        #循环接受客户端大小
            buf=client_conn.recv(1024)
            if len(buf) == 0:break
            print(client_conn.send(buf))
            print('客户端请求了%s'% buf)

            #print("连接地址：",client_addr)

            client_conn.close()

        tcp_socket.close()


# if __name__ == "__main__ ":
TcpServer()



# 执行报错 未解决，报错信息：
#    c_respons_data = tcp_client.recv(1024)
#ConnectionAbortedError: [WinError 10053] 您的主机中的软件中止了一个已建立的连接。