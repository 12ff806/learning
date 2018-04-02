#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Sin"

"""
follow.py

A generator that follows a log file like Unix "tail -f".
"""


import time


def follow(thefile):
    thefile.seek(0, 2)    # Go to the end of the file
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)    # Sleep briefly
            continue
        yield line


# Example use
if __name__ == "__main__":
    logfile = open("access-log")
    for line in follow(logfile):
        print(line,)


