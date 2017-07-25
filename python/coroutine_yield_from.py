#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 定义异常
class SpamException(Exception):
    pass


# yield from 实现生产者消费者模型
def consumer():
    print("CONSUMER START")
    r = ""
    try:
        while True:
            try:
                n = yield r
                print("[CONSUMER] Consuming %s..." % n)
                r = "Consuming %s [DONE]" % n
            except SpamException:
                print("[CONSUMER] catching SpamException")
    except GeneratorExit:
        print("CONSUMER EXIT")


def consumer_agent(c):
    try:
        print("CONSUMER AGENT START")
        yield from c
    except SpamException:  # 这个异常永远捕获不到, 因为调用者(produce)通过 yield from 将异常直接传递给了子迭代器, 也就是这里的 c
        print("CONSUMER AGENT CATCHING SPAMEXCEPTION")
    except GeneratorExit:
        #c.close()  # 并不需要手动关闭子迭代器, yield from 会自动将调用者(produce)发出的异常传递给子迭代器
        print("CONSUMER AGENT EXIT")


def produce(ca):
    ca.send(None)
    n = 0
    while n < 5:
        n += 1
        print("[PRODUCE]  Producing %s..." % n)
        if n == 2:
            ca.throw(SpamException)
        else:
            r = ca.send(n)
            print("[PRODUCE]  %s..." % r)
    ca.close()


c = consumer()
ca = consumer_agent(c)
produce(ca)


