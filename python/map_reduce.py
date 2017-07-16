#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from functools import reduce


CHAR_TO_INT = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
CHAR_TO_FLOAT = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, ".": -1}


# str to int
def str2int(s):
    ints = map(lambda ch: CHAR_TO_INT[ch], s)
    return reduce(lambda x, y: x * 10 + y, ints, 0)

print(str2int('0'))
print(str2int('1'))
print(str2int('12300'))
print(str2int('0012345'))


# str to float
def str2float(s):
    sign = 1;
    if s[0] == "-":
        s = s[1:]
        sign = -1
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0) * sign

print(str2float("0"))
print(str2float("123.456"))
print(str2float("123.45600"))
print(str2float("0.1234"))
print(str2float(".1234"))
print(str2float("120.0034"))
print(str2float("120.00"))
print(str2float("-120.00"))
print(str2float("-120.0034"))
print(str2float("-.1234"))
print(str2float("-0.1234"))


# 首字母大写, 其它转为小写
def normalize(name):
    #first_char = 1
    #def fn(s):
    #    nonlocal first_char
    #    if first_char == 1:
    #        first_char = 0
    #        return s.upper()
    #    else:
    #        return s.lower()
    #    
    #l = map(fn, name)
    #return "".join(l)

    return name[0].upper() + name[1:].lower()

L1 = ["adam", "LISA", "barT"]
L2 = list(map(normalize, L1))
print(L2)


# 传入list, 返回list项的积
def prod(L):
    return reduce(lambda x, y: x * y, L)

print("3 * 5 * 7 * 9 =", prod([3, 5, 7, 9]))
