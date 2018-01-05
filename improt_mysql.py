#! /usr/bin/env python
# -*- coding: utf-8 -*-# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/11/9

import pymysql


conn = pymysql.connect(host='192.168.64.131',port=3306,user='root',passwd='123456',db='makeblock',charset='utf8')

# 创建游标
cursor = conn.cursor()

re_row = cursor.executemany("INSERT into user(userid,username,userpassword)VALUES (%s,%s,%s )", [("1003", "u1name", "p1000"), ("1004", "u2name", "p1002")]
                        )
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()

#获取自增id
new_id = cursor.lastrowid
print (new_id)