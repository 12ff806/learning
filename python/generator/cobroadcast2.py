#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from coroutine import coroutine
import time


def follow(thefile, target):
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        target.send(line)

@coroutine
def grep(pattern, target):
    while True:
        line = (yield)
        if pattern in line:
            target.send(line)

@coroutine
def printer():
    while True:
        line = (yield)
        print(line)

@coroutine
def broadcast(targets):
    while True:
        item = (yield)
        for target in targets:
            target.send(item)

if __name__ == "__main__":
    f = open("access-log")
    p = printer()
    follow(f, broadcast([grep("python", p),
                         grep("ply", p),
                         grep("swig", p)]))
