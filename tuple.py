#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/11/16


# tuplea=(['11', "22"], 33, 44, 55)
#
#
# for i in tuplea:
#     #if i[0] ==list:
#     print(type(i[1]))
#      #print(str(i[0][1]))


a=[1,2,3,4]
b=["1",2]
c=a
# b=c
print("获取的是对象在内存中的地址")
print(id(a))
print(id(b))
print(id(c))

print("is 就是比对2个变量的对象引用是否指向同一个对象")
print(a is b)
print(a is c)

print("==：比对2个变量指向的对象的内容是否相同")
print(a ==b )

