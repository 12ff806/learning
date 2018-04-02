#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# If you call send() on an already-executing coroutine, your program will crash
# Multiple threads sending data into the same target coroutine

from cobroadcast import *
from cothread import threaded


p = printer()
target = broadcast([threaded(grep("foo", p)), threaded(grep("bar", p))])

for i in range(10):
    target.send("foo is nice\n")
    target.send("bar is bad\n")

del target
del p
