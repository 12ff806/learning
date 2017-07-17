#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from enum import Enum, unique


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

c = Color.RED
print(isinstance(c, Enum))
print(c)
print(Color.RED.value)


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
print("day1 =", day1)
