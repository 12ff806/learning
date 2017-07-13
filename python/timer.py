#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import time

#def foo():
#    print 'in foo()'
#
#foo()

#def foo():
#    start = time.clock()
#    print 'in foo()'
#    end = time.clock()
#    print 'used:', end - start
#
#foo()

#def foo():
#    print 'in foo()'
#
#def timer(func):
#    start = time.clock()
#    func()
#    end = time.clock()
#    print 'used:', end - start
#
#timer(foo)

#def foo():
#    print 'in foo()'
#
#def timer(func):
#    def wrapper():
#        start = time.clock()
#        func()
#        end = time.clock()
#        print 'used:', end - start
#
#    return wrapper
#
#foo = timer(foo)
#foo()

def timer(func):
    def wrapper():
        start = time.clock()
        func()
        end = time.clock()
        print 'used:', end - start

    return wrapper

@timer
def foo():
    print 'in foo()'

foo()
