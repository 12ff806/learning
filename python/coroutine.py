#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 协程的实现
def consumer():
    r = ""
    while True:
        n = yield r
        if not n:
            return
        print("[CONSUMER] Consuming %s..." % n)
        r = "200 OK"

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print("[PRODUCE] Producing %s..." % n)
        r = c.send(n)
        print("[PRODUCE] Consumer return: %s" % r)
    c.close()

c = consumer()
produce(c)


