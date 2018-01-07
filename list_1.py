#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2018/1/7



list = [1,2,1,2,1,2,1,2]

for x in list:

    if x ==1:
        list.remove(x)
print(list)

#print:[2,2,2]

list = [1,2,1,2,1,1,1]

for x in list:

    if x ==1:
        list.remove(x)
print(list)
