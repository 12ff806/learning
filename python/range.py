#!/usr/bin/env python3
# -*- coding: utf-8 -*-

for i in range(5):
    print(i)

for i in range(5, 10):
    print(i)

for i in range(0, 10, 3):
    print(i)

for i in range(-10, -100, -30):
    print(i)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

print(range(10)) # range() is not a list

print(list(range(10)))
