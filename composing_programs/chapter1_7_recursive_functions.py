#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sum_digits(n):
    """ Return the sum of the digits of positive integer n. """
    if n < 10:
        return n
    else:
        all_but_last, last = n // 10, n % 10
        return sum_digits(all_but_last) + last

print(sum_digits(1111))

################################################################

def fact_iter(n):
    total, k = 1, 1
    while k <= n:
        total, k = total * k, k + 1
    return total

print(fact_iter(4))

################################################################

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(4))

################################################################

def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n-1)

def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n-1)

print(is_even(4))
print(is_odd(4))

################################################################

def is_even(n):
    if n == 0:
        return True
    else:
        if (n-1) == 0:
            return False
        else:
            return is_even((n-1)-1)

print(is_even(6))

################################################################

def cascade(n):
    """Print a cascade of prefixes of n."""
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)

cascade(2013)

################################################################

def cascade(n):
    """Print a cascade of prefixes of n."""
    print(n)
    if n >= 10:
        cascade(n//10)
        print(n)

cascade(2013)

################################################################

def play_alice(n):
    if n == 0:
        print("Bob wins!")
    else:
        play_bob(n-1)

def play_bob(n):
    if n == 0:
        print("Alice wins!")
    elif is_even(n):
        play_alice(n-2)
    else:
        play_alice(n-1)

play_alice(20)
play_alice(19)
play_alice(18)
play_alice(12)

################################################################

def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

print(fib(10))

################################################################

def count_partitions(n, m):
    """Count the ways to partition n using parts up to m."""
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        return count_partitions(n-m, m) + count_partitions(n, m-1)

print(count_partitions(6, 4))
print(count_partitions(5, 5))
print(count_partitions(10, 10))
print(count_partitions(15, 15))
print(count_partitions(20, 20))


if __name__ == "__main__":
    pass

