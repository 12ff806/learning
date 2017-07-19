#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# __str__() 返回用户看到的字符串
class Student1(object):
    def __init__(self, name):
        self.name = name

print(Student1("Michael"))  # <__main__.Student1 object at 0x7fce6b53a4a8>
print("------------------------")


class Student2(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Student2 object (name: %s)" % self.name

print(Student2("Michael"))  # Student2 object (name: Michael)
s = Student2("Michael")
s  # <__main__.Student1 object at 0x7fce6b53a4a8>
   # 如果在python解释器中直接显示变量,调用的不是__str__(), 而是__repr__()
print("------------------------")



# __repr__() 返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的
class Student3(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Student3 object (name: %s)" % self.name

    __repr__ = __str__  # 偷懒写法, 通常__str__()和__repr__()的代码是一样的

s = Student3("Michael")
s  # Student2 object (name: Michael)
   # 调用的是 __repe__()
print("------------------------")



# __iter__() 如果一个类想被用于for ... in循环，
# 类似list或tuple那样，就必须实现一个__iter__()方法，
# 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法
# 拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
class Fib1(object):
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a

f = Fib1()
for i in f:
    print(i)
print("------------------------")



# __getitem__(): 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
class Fib2(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a

for i in range(10):
    print(Fib2()[i])
print("------------------------")


# __getitem__(): 实现下标和切片操作
# 没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的
# 此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值
# 最后，还有一个__delitem__()方法，用于删除某个元素
class Fib3(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for i in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            step = n.step
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for i in range(stop):
                if i >= start:
                    L.append(a)
                a, b = b, a + b
            return L

print(Fib3()[:10])
print(Fib3()[2:11])
print("------------------------")



# __getattr__() 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错
# 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性
# 注意，只有在没有找到属性的情况下,才调用__getattr__，已有的属性,不会在__getattr__中查找
class Student4(object):
    def __init__(self, name):
        self.name = name

    def __getattr__(self, attr):
        if attr == "score":
            return 99

stu = Student4("Michael")
print(stu.name)
print(stu.score)  # 99
print("------------------------")



# __getattr__() 返回函数
class Student5(object):
    def __init__(self, name):
        self.name = name

    # 注意到任意调用如stu1.score都会返回None，这是因为我们定义的__getattr__默认返回就是None
    # 要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误
    def __getattr__(self, attr):
        if attr == "age":
            return lambda: 25
        raise AttributeError("\"Student5\" object has no attribute \"%s\"" % attr)

stu1 = Student5("Michael")
print(stu1.name)
print(stu1.age())
try:
    print(stu1.score)  # AttributeError: "Student5" object has no attribute "score"
except AttributeError as e:
    print(e)
print("------------------------")



# __getattr__() 实现链式调用
class Chain(object):
    def __init__(self, path=""):
        self.__path = path

    def __getattr__(self, path):
        return Chain("%s/%s" % (self.__path, path))

    def __call__(self, path):
        return Chain("%s/%s" % (self.__path, path))

    def __str__(self):
        return self.__path

    __repr__ = __str__

print(Chain().status.user.timeline.list)
print(Chain().users("michael").repos)

