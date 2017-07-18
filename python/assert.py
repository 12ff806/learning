#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 关闭断言: python3 -O assert.py 就会把 assert 当成 pass

def foo(s):
    n = int(s)
    assert n != 0, "n is zero!"
    return 10 / n

def main():
    foo("0")

main()
