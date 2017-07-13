#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you hava any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    print(arguments)
    print(keywords)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Plain",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)                                             # 1 positional argument
parrot(voltage=1000)                                     # 1 keyword argument
parrot(voltage=1000000, action="VOOOOOM")                # 2 keyword arguments
parrot(action="VOOOOOM", voltage=1000000)                # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')            # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')     # 1 positional, 1 keyword
# all the following calls would be invalid:
#parrot()                                                # required argument missing
#parrot(voltage=5.0, 'dead')                             # non-keyword argument after a keyword argument
#parrot(110, voltage=220)                                # duplicate value for the same argument
#parrot(actor='John Cleese')                             # unknown keyword argument

def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a+b
    print()

fib(2000)
f = fib
f(100)
print(f(100))    # function fib returns 'None'

def fib2(n):    # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f2 = fib2(200)    # call fib2()
print(f2)    # print the result

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('Do you really want to quit?')
ask_ok('OK to overwrite the file?', 2)
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

i = 5

def f(arg=i):
    print(arg)

i = 6
f()

def f(a, L=[]):
    L.append(a)
    print(L)
    return L

f(1)
f(2)
f(3)

def f(a, L=None):
    print(L)
    if L is None:
        L = []
    L.append(a)
    print(L)
    return L

f(1)
f(2)
f(3)

