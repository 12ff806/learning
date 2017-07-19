#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):
    __slots__ = ("name", "age")  # 用tuple定义允许绑定的属性名称. __slots__定义的属性仅对当前类实例起作用

class GraduateStudent(Student):
    pass

s = Student()  # 创建新的实例
s.name = "Janus" # 创建属性name
s.age = 22 # 创建属性age

try:
    s.score = 99
except AttributeError as e:
    print("AttributeError:", e)

g = GraduateStudent()
g.score = 88  # __slots__ 对子类的实例没有作用
print("g.score =", g.score)

