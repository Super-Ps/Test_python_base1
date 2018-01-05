#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2017/9/12



name = 'PythonTab'
def func1():
    #print('my name is %s' %(name))
    name = 'PythonTab.com'
    print('my name is %s' %(name))
func1()
print(name)



name = 'default'
def func2():
    global name
    name = 'PythonTab.com'
    print(name)
func2()
print(name)



nameList =['Python','Tab','.com']
def func3():
    nameList[0] = 'python11'
func3()
print(nameList)



nameList =['Python','Tab','.com']
def func5():
    #gloabl nameList
    nameList = []
func5()
print(nameList)