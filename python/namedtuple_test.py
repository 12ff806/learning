#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Sin"



from collections import namedtuple


User = namedtuple("User", ["name", "sex", "age"])
user1 = User(name="Sin", sex="male", age="22")
user2 = User._make(["Janus", "male", 24])

print(user1)
print(user2)
print(user1.name)
print(user1.sex)
print(user1.age)

user1 = user1._replace(age=25)
print(user1)

print(user1._asdict())
