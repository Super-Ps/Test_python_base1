#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/9/18



# map(func,iter,iter)

# map()返回一个迭代器，迭代器的每个元素都是将列表或元组“seq”中的相应元素传入函数func返回的结果。



list_a = [1, 2, 1, 2, 3]

map_a = (map(lambda x: x+1, list_a))
#print((lambda x:x+1,list_a))

print(list(map_a))  #转化成列表输出



