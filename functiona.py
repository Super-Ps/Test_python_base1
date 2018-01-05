#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2017/9/8


#1
# def myfuc():
#
#     print("myfunc() called")
#
#
#
# myfuc()
# myfuc()

#2
# def deco(func):
#     print("before a")
#
#     func()
#     print("after a")
#
#     return func
#
#
# def myfunc():
#     print("myfunc() called")
#
#
# myfunc=deco(myfunc)
#
#
# myfunc()
# myfunc()

#3
# def deco(func):
#     print("before myfunc() a.")
#     func()
#     print("  after myfunc() b.")
#     return func
#
#
# @deco
# def myfunc():
#     print(" myfunc() called.")
#
#
# myfunc()
#myfunc()


#4''示例4: 使用内嵌包装函数来确保每次新函数都被调用，
#内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象'''
def deco(func):
    def _deco():
        print("before myfunc() a.")
        func()
        print("after myfunc() b.")
        # 不需要返回func，实际上应返回原函数的返回值

    return _deco


@deco
def myfunc():
    print("myfunc() ")
    #return 'ok'


myfunc()
myfunc()