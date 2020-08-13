#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#def square(x):
#    return x * x

#def sum_naturals(n):
#    total, k = 0, 1
#    while k <= n:
#        total, k = total + k, k + 1
#    return total

#def sum_cubes(n):
#    total, k = 0, 1
#    while k <= n:
#        total, k = total + k*k*k, k + 1
#    return total

#def pi_sum(n):
#    total, k = 0, 1
#    while k <= n:
#        total, k = total + 8 / ((4*k-3) * (4*k-1)), k + 1
#    return total

#print(sum_naturals(100))
#print(sum_cubes(100))
#print(pi_sum(100))

################################################################

def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def cube(x):
    return x*x*x

def sum_cubes(n):
    return summation(n, cube)


def identity(x):
    return x

def sum_naturals(n):
    return summation(n, identity)


def square(x):
    return x*x

def sum_square(n):
    return summation(n, square)


def pi_term(x):
    return 8 / ((4*x-3) * (4*x-1))

def pi_sum(n):
    return summation(n, pi_term)

print(sum_cubes(3))
print(sum_naturals(10))
print(sum_square(10))
print(pi_sum(1e6))

################################################################

def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def golden_update(guess):
    return 1/guess + 1

def square_close_to_successor(guess):
    return approx_eq(guess*guess, guess+1)

def approx_eq(x, y, tolerance=1e-15):
    return abs(x-y) < tolerance

phi = improve(golden_update, square_close_to_successor)
print(phi)

from math import sqrt
phi_test = 1/2 + sqrt(5)/2
def improve_test():
    approx_phi = improve(golden_update, square_close_to_successor)
    assert approx_eq(phi_test, approx_phi), "phi differs from its approximation"

improve_test()

################################################################

def average(x, y):
    return (x + y)/2

def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def approx_eq(x, y, tolerance=1e-3):
    return abs(x-y) < tolerance

def sqrt(a):
    def sqrt_update(x):
        return average(x, a/x)
    def sqrt_close(x):
        return approx_eq(x*x, a)
    return improve(sqrt_update, sqrt_close)

print(sqrt(64))

################################################################

def square(x):
    return x*x

def successor(x):
    return x + 1

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h

def f(x):
    """Never called."""
    return -x

square_successor = compose1(square, successor)
result = square_successor(12)
print(result)

################################################################

def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)
    return update

def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)

def square_root_newton(a):
    def f(x):
        return x * x - a
    def df(x):
        return 2 * x
    return find_zero(f, df)

print(square_root_newton(64))

################################################################

def power(x, n):
    """ Return x * x * x * ... * x for x repeated n times."""
    product, k = 1, 0
    while k < n:
        product, k = product * x, k + 1
    return product

def nth_root_of_a(n, a):
    def f(x):
        return power(x, n) - a
    def df(x):
        return n * power(x, n-1)
    return find_zero(f, df)

print(nth_root_of_a(2, 64))
print(nth_root_of_a(3, 64))
print(nth_root_of_a(6, 64))

################################################################

def curried_pow(x):
    def h(y):
        return pow(x, y)
    return h

print(curried_pow(2)(3))

################################################################

def map_to_range(start, end, f):
    while start < end:
        print(f(start))
        start = start + 1

map_to_range(0, 10, curried_pow(2))

################################################################

def curry2(f):
    """ Return a curried version of the given two-argument function. """
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

def uncurry2(g):
    """ Return a twe-argument version of the given curried function. """
    def f(x, y):
        return g(x)(y)
    return f

pow_curried = curry2(pow)
print(pow_curried(2)(5))
map_to_range(0, 10, pow_curried(2))

################################################################

print(uncurry2(pow_curried)(2, 5))

################################################################

def compose1(f, g):
    return lambda x: f(g(x))

f = compose1(lambda x: x * x, lambda y: y + 1)
result = f(12)
print(result)

################################################################

def trace(fn):
    def wrapped(x):
        print("-> ", fn, "(", x, ")")
        return fn(x)
    return wrapped

@trace
def triple(x):
    return 3 * x

triple(12)


if __name__ == "__main__":
    pass

