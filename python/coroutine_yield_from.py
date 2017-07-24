#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# yield from 实现生产者消费者模型
def consumer():
    print("CONSUMER START")
    r = ""
    try:
        while True:
            n = yield r
            print("[CONSUMER] Consuming %s..." % n)
            r = "Consuming %s [DONE]" % n
    except GeneratorExit:
        print("CONSUMER EXIT")


def consumer_agent(c):
    try:
        print("CONSUMER AGENT START")
        yield from c
    except GeneratorExit:
        c.close()
        print("CONSUMER AGENT EXIT")


def produce(ca):
    ca.send(None)
    n = 0
    while n < 5:
        n += 1
        print("[PRODUCE]  Producing %s..." % n)
        r = ca.send(n)
        print("[PRODUCE]  %s..." % r)
    ca.close()

c = consumer()
ca = consumer_agent(c)
produce(ca)


