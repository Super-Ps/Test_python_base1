#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/11/14

# 所有的生成器 都是迭代器，  迭代器不一定是生成器
# 列表。元祖，字符串，字典都是可迭代对象
# l=[1,2,3,4,5]
#
# i=iter(l)
#
# print(i)   # <list_iterator object at 0x002694D0>


# 什么是迭代器？
#
# 满足2个条件：1,,有iter方法  2有next方法

# print(next(i))
# print(next(i))
# print(next(i))

def add(x,y):
    return x+y


def gen():

    for i in range(4):
        yield  i


base=gen()
for n in(1,10):
    base=(add(i,n) for i  in base)

print(list(base))
