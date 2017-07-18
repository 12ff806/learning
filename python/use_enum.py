#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from enum import Enum, unique


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED)  # 颜色枚举成员, 属于颜色枚举类型
print(dir(Color.RED))  # 查看Color.RED的所有属性
print(Color.RED.name)  # 通过成员来访问成员名称
print(Color.RED.value)  # 通过成员来访问成员值
print(Color(1))  # 通过成员值来访问成员
print(Color(3))  # 通过成员值来访问成员
print(Color["RED"])  # 通过成员名称来访问成员
print("++++++++++++++++++++++")
print("type(Color.RED) ==", type(Color.RED))
print("type(Color) ==", type(Color))
print("hasattr(Color, \"RED\") ==", hasattr(Color, "RED"))
print("isinstance(Color.RED, Color) ==", isinstance(Color.RED, Color))
print("isinstance(Color.RED, Enum) ==", isinstance(Color.RED, Enum))
print("isinstance(Color, Enum) ==", isinstance(Color, Enum))
print("++++++++++++++++++++++")


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
