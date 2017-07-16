#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 构造从3开始的无限奇数序列生成器
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 定义筛选(埃氏筛法)函数
def _not_divisible(n):
    return lambda x: x % n > 0


# 素数生成器
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


for i in primes():
    if i < 1000:
        print(i)
    else:
        break
