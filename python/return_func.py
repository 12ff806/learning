#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 返回的是求和函数
def lazy_sum(*args):
    def sum():
        s = 0
        for i in args:
            s = s + i
        return s
    return sum

f = lazy_sum(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f)
print(f())


# 返回列表,列表值为三个函数
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1())  # 9
print(f2())  # 9
print(f3())  # 9


# 修复上面count函数的bug
def new_count():
    fs = []
    def f(n):
        def g():
            return n * n
        return g
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f4, f5, f6 = new_count()
print(f4())  # 1
print(f5())  # 4
print(f6())  # 9

