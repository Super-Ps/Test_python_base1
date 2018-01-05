#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/9/18


import  socket

# 第一步创建socket对象，调用scoket函数
# family   1.AF_INET家族包括Internet地址   2.AF_UNIX家族用于同一台机器上的进程间通信
# type 1.SOCK_STREAM(流套接字)  2.SOCK_DGRAM(数据报套接字)

#socket=socket.socket(family=,type=)


# 第二步是将socket绑定到指定地址。这是通过socket对象的bind方法来实现的

# 参数必须是一双元素元祖，格式(host,port) 分别代表主机，端口号，如果端口号正在使用，主机名不正确，bind方法印发socket.error异常

#socket.bind(address=(host,port))

# 第三步是使用socket套接字的listen方法接收连接请求
# backlog指定最多允许多少个客户连接到服务器。它的值至少为1。收到连接请求后，这些请求需要排队，如果队列满，就拒绝请求
#socket.listen(backlog=1)





if __name__ == '__main__':
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8001))
    sock.listen(5)
    while True:

        connection,address = sock.accept()
        try:
            connection.settimeout(5)
            buf = connection.recv(1024)
            if buf == '1':
                connection.send('welcome to server!')
            else:
                connection.send('please go out!')
        except socket.timeout:
            print ('time out')
        connection.close()
