#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/11/13


from locust_test import  mysql_slelect_a

import  time


# 拿到数据库的行数， 生成迭代对象后，每次拿的是所有行的数据，并不能分开拿，因为数据库查询是一次查询出来的总行数

# re_data=mysql_slelect_a.selectdata(10)
# print(re_data)
#
# for x in range(1, 10):
#
#     print(next(re_data))


# g=(j*2 for j in (55,992,66,55 ))
#
# print(g)
#
# print(type(next(g)))
# print(next(g))
# print(next(g))
# print(next(g))

# ============================================================

#   斐波那契数列  实现：

   #数据规律：0,1，  1,2,3,5,8,13,21.......

#  普通算法：

# def Fibonacci(sequence):
#
#     n,befor,after =0,0,1
#
#     while n<sequence:
#         befor,after = after,befor+after
#         #print(after)
#         #print(befor)
#         n+=1

#  斐波那契数列  yield 写法
#
# def Fibonacci(sequence):
#
#
#     n,befor,after =0,0,1
#
#     while n<sequence:
#
#         yield  befor # 生成器对象，没有在内存里面
#
#         befor,after = after,befor+after
#
#         n+=1
#
#
# g=Fibonacci(8)
# print(g)
#
# # 挨个拿生成器里面的数据，拿的时候才计算
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# ============================================================================================
# yield 最大的作用是保存状态， 对比return 来说，他执行完了就结束了，而yield 是接着执行
# 协成的是基于 yield实现的
#
# def bar():               # 步骤1，函数读在内存
#
#
#     print('ok1')        # 步骤3 执行print， yield
#     count = yield 1      # 步骤5 ，记录了上一步的状态，从这里执行，把传递进来的值给到 count=2222222
#
#     print(count)        # 步骤5.1 打印传递进来的值2222222
#
#     print('ok2')
#
#     count2 =yield 2
#     print(count2)
#
#     print('ok3')
#
#     count3 = yield 3
#     print(count3)
#
# g=bar()
# # print(g)
# # print(next(g))
#
# g.send(None)   #  相当于 next(g) 注意点是：第一次send前如果没有next(),自能传递None
#                # 步骤2,
#
# g.send(2222222) # 步骤4，这时候才传递值进去到yield
# g.send(33333)
# g.send(44444)

# ==================================伪并发实现=======================================
def coustme(name):

    print("%s 准备吃包子拉！" %name)
    while True:

        baozi = yield

        print("包子[%s]来了，被[%s]吃了！"%(baozi,name))





def pordcut():

    gen_a=coustme('A')
    gen_b=coustme('B')

    next(gen_a)
    next(gen_b)
    print("厨师准备开始做包子了！")
    for i in range(1,11):
        time.sleep(1)
        print('发送2次send复制给生成器')
        gen_a.send(i)
        gen_b.send(i)


pordcut()


