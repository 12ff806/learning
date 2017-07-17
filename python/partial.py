#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import functools


# 偏函数的功能即简化函数的参数
# 通过固定住函数的某些参数来创建一个新的函数
# 在这里即将int函数的base参数固定为2换回新的函数int2
int2 = functools.partial(int, base=2)
print(int2("100010"))  # 34


# 将10作为*args的一部分自动添加到左边
max2 = functools.partial(max, 10)
print(max2(5, 6, 7))  # 10 相当于 args = (10, 5, 6, 7)  max(*args)

