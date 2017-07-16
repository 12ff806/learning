#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 判断是否为奇数
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 9, 10, 15])))  # [1, 3, 5, 9, 15]


# 判断空字符串
def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ["A", "", "B", None, "C", "   "])))
