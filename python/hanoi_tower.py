#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def hanoi(n, a, b, c):
    if n == 1:
        print("move", a, "--->", c)
    else:
        hanoi(n-1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n-1, b, a, c)


hanoi(3, "A", "B", "C")
