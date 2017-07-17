#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# class Point
class Point:
    """ define a Point class """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

p = Point(3, 4)
print(p.x, p.y, p.distance_from_origin())
print("=============================")



# class Student
class Student(object):
    """ define a Student class """
    def __init__(self, name, score):
        # 用 __ 开头来定义私有属性, 确保只有内部可以访问, 外部不能访问
        # 实际上是 __name 属性被python解释器改了名字(_Student__name), 导致访问不了
        # 但强烈不建议直接访问或修改被改后的属性名_Student__name
        # 因为不同的解释器可能改成了不一样的名字
        self.__name = name    
        self.__score = score

    def print_score(self):
        print("%s: %s" % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def get_grade(self):
        if self.__score >= 90:
            return "A"
        elif self.__score >= 60:
            return "B"
        else:
            return "C"

    def set_score(self, score):
        if score >= 0 and score <= 100:
            self.__score = score
        else:
            raise ValueError("bad score")

bart = Student("Bart Simpson", 59)
lisa = Student("Lisa Simpson", 90)
bart.print_score()
print(bart._Student__name)  # 实际访问的是 __name 私有属性, 属性名被解释器改成了 _Student__name
print(bart.get_name())
print(bart.get_grade())
bart.set_score(80)
print(bart.get_score())
print(bart.get_grade())
lisa.print_score()
print(lisa.get_grade())
print("=============================")



# class Animal
class Animal(object):
    """ define a Animal class """
    def run(self):
        print("Animal is running....")

class Dog(Animal):
    """ define a Dog class inherit from Animal """
    def run(self):
        print("Dog is running....")

    def eat(self):
        print("Eating meat....")

class Cat(Animal):
    """ define a Cat class inherit from Animal """
    def run(self):
        print("Cat is running....")

def run_twice(animal):
    animal.run()
    animal.run()

dog = Dog()
dog.run()
cat = Cat()
cat.run()

a = Animal()
d = Dog()
c = Cat()

# 判断对象信息.对于class的继承关系来说,使用type()就很不方便.判断class的类型,使用isinstance()函数
print("a is Animal?", isinstance(a, Animal))
print("a is Dog?", isinstance(a, Dog))
print("a is Cat?", isinstance(a, Cat))

print("d is Animal?", isinstance(d, Animal))
print("d is Dog?", isinstance(d, Dog))
print("d is Cat?", isinstance(d, Cat))

run_twice(c)
print("=============================")


# 获取基本类型信息,可使用type()函数,也可使用isinstance()函数
print("type(123) =", type(123))
print("type(\"123\") =", type("123"))
print("type(None) =", type(None))
print("type(abs) =", type(abs))
print("type(123)==int?", type(123)==int)
print("type(\"abc\")==str?", type("abc")==str)
print("type(123)==type(456)?", type(123)==type(456))
print("type(123)==type(\"123\")?", type(123)==type("123"))
import types
def fn():
    pass
print("type(fn)==types.FunctionType?", type(fn)==types.FunctionType)
print("type(abs)==types.BuiltinFunctionType?", type(abs)==types.BuiltinFunctionType)
print("type(lambda x: x)==types.LambdaType?", type(lambda x: x)==types.LambdaType)
print("type((x for x in range(10)))==types.GeneratorType?", type((x for x in range(10)))==types.GeneratorType)
print("isinstance(123, int) ==", isinstance(123, int))
print("isinstance(\"abc\", str) ==", isinstance("abc", str))
print("isinstance(b\"a\", bytes) ==", isinstance(b"a", bytes))
# 还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple
print("isinstance([1,2,3], (list, tuple)) ==", isinstance([1,2,3], (list, tuple)))
print("isinstance((1,2,3), (list, tuple)) ==", isinstance((1,2,3), (list, tuple)))
