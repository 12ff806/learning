#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def rational(n, d):
    return [n, d]

def numer(x):
    return x[0]

def denom(x):
    return x[1]

def add_rationals(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rationals(x, y):
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def print_rational(x):
    print(numer(x), "/", denom(x))

def rationals_are_equal(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)

from fractions import gcd
def rational(n, d):
    g = gcd(n, d)
    return (n//g, d//g)

def square_rational(x):
    return mul_rational(x, x)

def pair(x, y):
    """Return a function that represents a pair."""
    def get(index):
        if index == 0:
            return x
        elif index == 1:
            return y
    return get

def select(p, i):
    """Return the element at index i of pair p."""
    return p(i)


if __name__ == "__main__":
    half = rational(1, 2)
    print_rational(half)
    third = rational(1, 3)
    print_rational(mul_rationals(half, third))
    print_rational(add_rationals(third, third))
    p = pair(20, 14)
    print(select(p, 0))
    print(select(p, 1))

