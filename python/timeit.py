#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import time

def timeslong(func):
    start = time.clock()
    print "It's time starting!"
    func()
    print "It's time ending!"
    end = time.clock()
    return "It's used: %s ."%(end-start)

def func():
    print "It's in func()"

print timeslong(func)
