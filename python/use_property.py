#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 属性检查的一般实现
class Student1(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be an integer!")
        if value > 100 or value < 0:
            raise ValueError("socre must between 0 and 100!")
        self._score = value

s1 = Student1()
s1.set_score(89)
print(s1.get_score())
# ValueError: score must between 0 and 100!
# s1.set_score(9999)
print("===============================")




# 利用@property实现属性检查
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be an integer!")
        if value < 0 or value > 100:
            raise ValueError("score must between 0 and 100!")
        self._score = value

s = Student()
s.score = 60
print("s.score =", s.score)
# ValueError: score must between 0 and 100!
#s.score = 9999 
print("===============================")




# 定义只读属性
class Student2(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2017 - self._birth

s3 = Student2()
s3.birth = 1992
print(s3.birth)  # birth是可读写属性
print(s3.age)  # age是只读属性
#s3.age = 20  # AttributeError: can't set attribute




# 定义一个Screen类
class Screen(object):
    """ define a Screen class """
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._height * self._width

screen = Screen()
screen.width = 1024
screen.height = 768
print(screen.width)
print(screen.height)
print(screen.resolution)
assert screen.resolution == 786432, '1024 * 768 = %d ?' % screen.resolution


