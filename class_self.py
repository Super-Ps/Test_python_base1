#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2018/1/3



class Bar(object):
    ''' 因为 self == 对象b ，所以在外面设置 对象name属性后 可以再方法内部调用'''
    def __init__(self):
        pass

    def foo(self,args):
        print(self,args,self.name)


b=  Bar()


b.name ="jonny"

b.foo(555)