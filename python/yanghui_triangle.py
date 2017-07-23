#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# example 1
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

print("-------------------")


# example2
def triangle1(max):
    n = 0
    l = [1]
    while n < max:
        yield l
        l.append(0)
        l = [l[i-1]+l[i] for i in range(len(l))]
        n = n + 1
    return "Done"

for x in triangle1(10):
    print(x)

print("-------------------")

g = triangle1(10)
while True:
    try:
        x = next(g)
        print(x)
    except StopIteration as e:
        print(e.value)
        break

