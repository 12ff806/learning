#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
grep.py

A very simple coroutine
"""


def grep(pattern):
    print("Looking for %s" % pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)


if __name__ == "__main__":
    g = grep("python")
    g.__next__()    # next(g) / g.send(None)
    g.send("Yeah, but no, but yeah, but no")
    g.send("A series of tubes")
    g.send("python generators rock!")
