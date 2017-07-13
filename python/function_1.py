#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######## DocStrings

def print_max(x, y):
    """Prints the maximum of two numbers.
    The two values must be integers."""
    # convert to integers, if possible
    x = int(x)
    y = int(y)

    if x > y:
        print(x, "is maximum")
    else:
        print(y, "is maximum")

print_max(3, 5)
print(print_max.__doc__)


######## the return statement

def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return "The numbers are equal"
    else:
        return y

print(maximum(2, 3))


######## variable number of arguments

def total(a=5, *numbers, **phonebook):
    print("a", a)

    for single_item in numbers:
        print("single item", single_item)

    for first_part, second_part in phonebook.items():
        print(first_part, second_part)

total(10,1,2,3,Jack=1123,John=2231,Inge=1560)


######## Keyword Arguments

def func2(a, b=5, c=10):
    print("a is", a, "and b is", b, "and c is", c)

func2(3, 7)
func2(25, c=24)
func2(c=50, a=100)


######## Default Argument Values

def say(message, times=1):
    print(message * times)

say("hello")
say("world", 5)


######## the global statement

x = 50

def func1():
    global x
    print("x is", x)
    x = 2
    print("Changed global x to", x)

func1()
print("value of x is", x)


######## Local Variables

x = 50

def func(x):
    print('x is', x)
    x = 2
    print("Changed local x to", x)

func(x)
print("x is still", x)


######## Function Parameters

def print_max(a, b):
    if a > b:
        print(a, "is maximum")
    elif a == b:
        print(a, "is equal to", b)
    else:
        print(b, "is maximum")

# directly pass literal values
print_max(3, 4)

x = 5
y = 7
# pass variables as arguments
print_max(x, y)


######## Functions

def say_hello():
    # block belonging to the function
    print("hello world")
# End of function

say_hello()    # call the function
say_hello() # call the function again
