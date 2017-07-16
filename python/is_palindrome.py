#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 判断回文数 方法一
def is_palindrome1(n):
    n = str(n)
    for i in range(len(n)//2):
        #if not (n[i] == n[-(i+1)]):
        if not (n[i] == n[len(n)-1-i]):  
            return False
    return True

# 判断回文数 方法二
def is_palindrome2(n):
    return str(n) == str(n)[::-1]

print(list(filter(is_palindrome1, range(1, 10000))))
print(list(filter(is_palindrome2, range(1, 10000))))
