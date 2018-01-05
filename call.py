#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/12/26




class jonny(object):

    def __init__(self,*args):
        self.a = args
        print(self.a)
        print(type(self.a))


    def __call__(self, *args):
        sums = 0
        for i in self.a:

            sums += i
        return sums



j = jonny()



#p=j.__call__()

#print

print(a)
print(a())