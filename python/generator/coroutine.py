#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
coroutine.py

A decorator function that takes care of starting a coroutine
automatically on call.
"""


def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.send(None)
        return cr
    return start


if __name__ == "__main__":
    @coroutine
    def grep(pattern):
        print("Looking for %s" % pattern)
        while True:
            line = (yield)
            if pattern in line:
                print(line)

    g = grep("python")    # coroutine(grep)("python")
    g.send("Yeah, but no, but yeah, but no")
    g.send("A series of tubes")
    g.send("python generators rock!")
