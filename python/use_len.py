#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()

# len()函数内部,会自动去调用dog 对象的__len__()方法,所以下面的代码是等价的
print(len(dog))  
print(dog.__len__())


