#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def triangle():
    L = [1];
    while True:
        yield L
        L.append(0);
        L = [L[i-1] + L[i] for i in range(len(L))]


n = 0
for t in triangle():
    if(n == 10):
        break
    print(t)
    n = n + 1
