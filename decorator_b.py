#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/11/10

# 装饰器过程 分解：

import time


# 写代码的原则： 对修改封闭(不应该修改原代码)，对扩展开放（在原有代码上扩展）
# 装饰器就是给原函数添加新的功能



def show_time(funcname):  #被传递动态的函数名

    def inner():
        start = time.time()

        funcname() # 替换了写死的函数调用

        end = time.time()

        print('执行了%s 秒' % (end - start))

    return inner



#foo = show_time(foo)
@show_time
def foo():

    time.sleep(2)
    print('foo.....')


foo()

def bar():

    time.sleep(3)
    print('bar.....')



#show_time(foo)   #传递函数名

#print(show_time(foo))  输出的是一个inner函数地址

# foo = show_time(foo)
# foo()      # 执行 inner函数
# bar = show_time(bar)
# bar()       # 执行 inner函数


