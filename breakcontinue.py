#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "ps"
# Email: master@liwenzhou.com
# Date: 2017/9/12

# break

for n in range(2, 10):
    for x in range(2, n):

        if n % x == 0:

            print(n, 'erquals', x, '*', n//x)

            break
    else:

        print(n, '单数')


# continue

for num in range(2, 10):

    if num % 2 == 0:

        print('余数为0的', num)
        continue
    print('余数不为0的', num)