#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "jonny"
# Email: jonnyps@yeah.net
# Date: 2017/9/4


set1=set('jonnyps@yeah.net')
set2=set('jonnyps@yeah.net')

print(set1)

set1.add('22,2211')

print(set1)


set3=set1.issubset(set2)
set4=set1.issuperset(set2)

set11=set1.update('hello','1988abc')
print(set3)
print(set4)
print(set1)