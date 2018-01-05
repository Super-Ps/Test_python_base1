#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "jonny"
# Email: jonnysps@yeah.net
# Date: 2017/9/16
#
# l = ['a', 'b', 'c', 1, 2, 3]
#
#
#
#
# i=l.__iter__()     #调用迭代器方法生成迭代器对象
#
# print(i.__next__()) #访问next方法取出值
# print(i.__next__())
#
# i=iter(l)
# x=iter(l)
# print(i)
# print(x)
#
# print(next(i))
# print(next(x))
# print(next(i))
# print(next(x))


# 生成列表数据   方式1：
def func_a():

    list_a = []

    for x in range(10):

        list_a.append(x)

    return  list_a


def func_b():
    i=(x for x in range(10)) #生成器表达式就是把列表推导式的 []换成了 ():
    return i    #得到一个生成器

print(func_b())

# yield关键字

def func_c(N):   # 定义一个通过yield关键字返回值的函数

    for x in range(N):

        yield  x**2      #返回符合条件的数据

f=func_c(10)
print(f)
for item in f:
#f=func_c() #调用函数
    print(item)  #得到生成器


