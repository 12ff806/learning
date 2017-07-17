#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()

print("hasattr(obj, \"x\") =", hasattr(obj, "x")) # obj对象有属性x吗?
print("hasattr(obj, \"y\") ==", hasattr(obj, "y")) # obj对象有属性y吗?
print("setattr(obj, \"y\", 19)")
setattr(obj, "y", 19) # 给obj设置一个y属性
print("hasattr(obj, \"y\") ==", hasattr(obj, "y")) # obj对象有属性y吗?
print("getattr(obj, \"y\") ==", getattr(obj, "y")) # 获取属性y的指
print("getattr(obj, \"z\") ==", getattr(obj, "z", 404)) # 获取属性z的值,如果属性z不存在,则返回404
print("hasattr(obj, \"power\") ==", hasattr(obj, "power")) # obj对象有power属性吗?
print("getattr(obj, \"power\") ==", getattr(obj, "power")) # 获取属性power的值
fn =  getattr(obj, "power") # 获取属性power的值,并赋值给fn,fn指向obj.power
print(fn()) # 调用fn() 与调用obj.power()是一样的

