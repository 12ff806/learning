#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle
from coroutine import coroutine


@coroutine
def sendto(f):
    try:
        while True:
            item = (yield)
            pickle.dump(item, f)
            f.flush()
    except StopIteration:
        f.close()


def recvfrom(f, target):
    try:
        while True:
            item = pickle.load(f)
            target.send(item)
    except EOFError:
        target.close()


if __name__ == "__main__":
    import xml.sax
    from cosax import EventHandler
    from buses import *

    import subprocess
    p = subprocess.Popen(["python3", "busproc.py"], stdin=subprocess.PIPE)
    xml.sax.parse("allroutes.xml", EventHandler(buses_to_dicts(sendto(p.stdin))))
