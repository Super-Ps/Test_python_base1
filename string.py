#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2017/9/13


#字符排序
s = 'string'

l = list(s)

print(l)
l.sort()

print(l)

s = "".join(l)

print(s)

print(complex(55, 22))


a='a'
b='b'

c=''.join(b)

print(c)

seq4 = {'hello':1,'good':2,'boy':3,'doiido':4}

print(type(':'.join(seq4)))

d='abcdffe 1 12 2 3ddss'
d_s=d.split()

print(type(d_s))
print(d_s.reverse())

print('/'.join(d_s))

print(d_s.reverse())