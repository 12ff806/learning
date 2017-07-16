#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import functools


# example 1
def makeitalic(fn):
    @functools.wraps(fn)
    def wrapped1():
        return "<i>" + fn() + "</i>"
    return wrapped1


def makebold(fn):
    @functools.wraps(fn)
    def wrapped2():
        return "<b>" + fn() + "</b>"
    return wrapped2


@makebold
@makeitalic
def hello():
    return "hello world"


print(hello())
print(hello.__name__)  # hello

print("=============================")



# example 2
def log1(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        print("call %s():" % fn.__name__)
        return fn(*args, **kw)
    return wrapper


@log1
def now(name):
    return "hello " +  name + " 2017-07-16"


print(now("Sin"))
print(now.__name__)

print("=============================")



# example 3
def log2(text):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kw):
            print("%s %s:" % (text, fn.__name__))
            return fn(*args, **kw)
        return wrapper
    return decorator


@log2("execute")
def hi(name):
    return "hello " + name + "!"


print(hi("Janus"))

print("=============================")



# example 4
def log3(arg):
    if isinstance(arg, str):
        def decorator(fn):
            def wrapper(*args, **kw):
                print("begin %s %s." % (arg, fn.__name__))
                fn_value = fn(*args, **kw)
                print("end %s %s." % (arg, fn.__name__))
                return fn_value
            return wrapper
        return decorator
    else:
        def wrapper(*args, **kw):
            print("begin call %s." % arg.__name__)
            fn_value = arg(*args, **kw)
            print("end call %s." % arg.__name__)
            return fn_value
        return wrapper


@log3
def test1(name):
    print("hello %s !" % name)
    return "test1 Done"


@log3("execute")
def test2(name):
    print("hello %s !" % name)
    return "test2 Done"


v1 = test1("Sin")
print(v1)
print("=============================")
v2 = test2("Sin")
print(v2)


