#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/10/9

import  socket


client = socket.socket()

ip_port = ('127.0.0.1', 8818)

client.connect(ip_port)

while True:
    data = client.recv(1024).decode()
    print(data)

    input_data = input('客户端输入：')
    client.send(input_data.encode("utf-8 "))

    if input_data == 'exit':
        break