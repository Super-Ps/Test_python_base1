#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2017/9/13


d = {'name1': 'python', 'name2': 'java', 'name3': 'javascript'}


for keya in d:

    print(keya, 'value:', d[keya])


print(d.items())


for keya, value in d.items():

    print(keya,value)