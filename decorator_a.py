#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/11/10

# 学习地址：http://www.cnblogs.com/rhcad/archive/2011/12/21/2295507.html


# 1.作用域

# 遵循规则：  L<局部变量> E<检讨局部变量> G<全部变量> B<python内部提供>

# 2.高阶函数 ，满足其中1个就是高阶函数

# 2.1.函数名可以作为参数参数
# 2.2.函数名可以作为返回值

# def foo():
#
#     return print('foo')
# a =foo
# a()


# 闭包

# 关于闭包： 闭包= 内部函数快+ 定义函数时的环境
def outer():
    x = 10

    def inner():  # 条件1：内部函数
        print(x)  # 条件2：对外部作用域的变量进行引用

    return inner   #结论： 内部函数inner就是一个闭包


# 调用方式1：
# f=outer()   解析：outer()拿到的是 返回inner 这个变量，再将其赋值给f，
# f()        解析： f() 等于inner()调用

# 调用方式2：
# outer()() 解析： 简写上面的步骤

# inner()  # 直接调用内部函数 报错，全局无法调用

#  假如是已参数的形式传递进来，那么这个x 跟 x=10 是一样的，

# def outer1(x):
#
#     def inner():
#         print(x)
#
#     return inner
#
#
# outer1(8)()    #解析：传递参数8，等于x=8




