#!/usr/bin/env python3
# -*- coding: utf-8 -*-

age = 20
name = "Sins"

print("{0} was {1} years old  when he read this book".format(name, age))
print("Why is {0} playing with that python?".format(name))

print("{} was {} years old when he read this book".format(name, age))
print("Why is {} playing with that python?".format(name))

# decimal (.) precision of 3 for float '0.333'
print("{0:.3f}".format(1.0/3))
# fill with underscores (_) with the text centered
# (^) to 11 width "___hello___"
print("{0:_^11}".format("hello"))
# keyword-based "Sins read A Byte of Python"
print("{name} read {book}".format(name="Sins", book="A Byte of Python"))

print("a", end="")
print("b", end=" ")
print("c", end="")
print("\n", end="")
