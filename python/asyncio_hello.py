#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import asyncio
import threading
import time


@asyncio.coroutine
def hello():
    print("Hello world! (time: %s) (%s)" % (time.time(), threading.currentThread()))
    r = yield from asyncio.sleep(2)
    print("Hello again! (time: %s) (%s)" % (time.time(), threading.currentThread()))


@asyncio.coroutine
def hello1():
    print("Hello 1! (time: %s) (%s)" % (time.time(), threading.currentThread()))
    r = yield from asyncio.sleep(5)
    print("Hello 1 again! (time: %s) (%s)" % (time.time(), threading.currentThread()))


@asyncio.coroutine
def hello2():
    for i in range(10):
        print("hello %s (time: %s) (%s) " % (i, time.time(), threading.currentThread()))


@asyncio.coroutine
def hello3():
    print("Hello 3!!! (time: %s) (%s)" % (time.time(), threading.currentThread()))
    yield from asyncio.sleep(0.000000000000000000000000000000000000000000000000000000001)
    print("Hello 3 again!!! (time: %s) (%s)" % (time.time(), threading.currentThread()))


loop = asyncio.get_event_loop()
#task = [hello3(), hello2(), hello1(), hello()]
task = [hello(), hello1(), hello2(), hello3()]
loop.run_until_complete(asyncio.wait(task))
loop.close()


