#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 定义修饰器, 为协程首次自动执行next()
def coroutine(fun):
    def start(*args, **kw):
        g = fun(*args, **kw)
        g.send(None)
        return g
    return start


@coroutine
def grep(pattern):
    print("Looking for %s" % pattern)
    try:
        while True:
            line = yield
            if pattern in line:
                print(line)
    except GeneratorExit:
        print("COROUTINE GREP EXIT")


g = grep("python")  # grep("python") == coroutine(grep)("python") == start("python")
#g.send(None)
g.send("a line contains python.")
g.send("a line contains perl.")
g.close()



