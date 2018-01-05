#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "jonny"
# Email: jonnysps@yeah.net
# Date: 2017/9/14



d = lambda x:x+1 if x > 0 else 'error'

print(d(1))


dic_a = {"aaa": 123, "bbb": 456}

def func2(*kargs,**kwargs):
    print(kargs)
    print(kwargs)

    return kargs

def func3(*kargs,**kwargs):

    return kwargs



print("func2：", func2(2,3,4,5,5,6,['a','b',88,99],{100:111,200:222},ddd=222,fff="sssd"))

print(func3(aaa=123,bbb=456))

print(func3(dic_a))



