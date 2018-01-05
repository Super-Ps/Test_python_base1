#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/9/15


def func_list():

    list_a=['a','b','c','d']
    list_c=['Iloveyou','ifuckyou','q_q']

    list_b=[x+'jonny' for x in list_a]
    print(list_b)


def func_a():
    list1_b=[]
    list1_c=[x+1 for x in range(10) if x%2 !=0 ]

    print(list1_c)



def func_c():

    list1=[10,20,30]
    list2=[9,8,7]

    list4=['A', 'B', 'C']
    list5=['a', 'b', 'c']

    list3=[x*y for x in list1 for y in list2] #把list1和list2中的元素进行运算

    list6=[z+q for z in list4 for q in list5] #把list4和list5中的元素进行拼接

    print(list3)
    print(list6)


# 列表推导式 可以加入函数
def fun_dd(n):



    return n**2


def fun_d():

    list7 = [11,22,33,44,55]
    a=[fun_dd(x) for x in list7]
    print(a)



# func_list()
# func_a()
# func_c()

fun_d()