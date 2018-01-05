#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2018/1/3

# self 代指类对象，谁调用它，他就等于调用者
# class Dog(object):
#     ''' 验证self, 与对象实例 是一个地址  ，所以他们两者是相等的 '''
#     b=None
#     print("b被复制为：%s"%b)
#
#     def __init__(dog_self):
#         print("init the dog")
#         print("类对象地址是%s"%dog_self)
#         global b
#         b=dog_self
#         print("b全局设定后被复制%s"%b)
#
# d=Dog()
# print("实例地址是%s"%d)
# if d==b:
#     print("相等")
# else:
#     print("不相等")
#输出：
# b被复制为：None
# init the dog
# 类对象地址是<__main__.Dog object at 0x004A56D0>
# b全局设定后被复制<__main__.Dog object at 0x004A56D0>
# 实例地址是<__main__.Dog object at 0x004A56D0>
# 相等


# class Human(object):
#     ''' 1.类属性被 对象实例共享
#         2.对象的属性被赋值后不修改类属性 '''
#
#     name="jonny"
#     age = 18
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# print(Human.name)   # jonny
# print(Human.age)   # 18
#
# h1 = Human("yuchao", 22)
# print(h1.name, h1.age)   #yuchao 22
# h2 = Human("yueyue", 12)
# print(h2.name, h2.age)   #yueyue 12
#
# print(Human.name, Human.age)  #jonny 18






