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

from math import sqrt
phi_test = 1/2 + sqrt(5)/2
def improve_test():
    approx_phi = improve(golden_update, square_close_to_successor)
    assert approx_eq(phi_test, approx_phi), "phi differs from its approximation"


if __name__ == "__main__":
    #print(sum_naturals(100))
    #print(sum_cubes(100))
    #print(pi_sum(100))
    print(sum_cubes(3))
    print(sum_naturals(10))
    print(sum_square(10))
    print(pi_sum(1e6))
    phi = improve(golden_update, square_close_to_successor)
    print(phi)
    improve_test()

