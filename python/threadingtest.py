#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = "Sin"


import threading, time


def loop():
    print("thread %s is running...." % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print("thread %s >>> %s" % (threading.current_thread().name, n))
        time.sleep(1)
    print("thread %s ended." % threading.current_thread().name)


print("thread %s is running...." % threading.current_thread().name)
t = threading.Thread(target=loop, name="LoopThread")
t.start()
t.join()
print("thread %s ended." % threading.current_thread().name)


# part 2
balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        lock.acquire()
        # try...finally 确保锁一定会被释放
        try:
            change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)


# part 3
import threading, multiprocessing

def loop_copy():
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop_copy)
    t.start()

