#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = "Sin"


import threading, time


class MyThread(threading.Thread):
    def __init__(self):
        #threading.Thread.__init__(self)
        #super(MyThread, self).__init__()
        super().__init__()

    def run(self):
        global n, lock
        time.sleep(3)
        if lock.acquire():
            print(n, self.name)
            n = n + 1
            lock.release()


if __name__ == "__main__":
    n = 1
    ThreadList = []
    lock = threading.Lock()
    for i in range(1, 200):
        t = MyThread()
        ThreadList.append(t)

    for t in ThreadList:
        t.start()
    for t in ThreadList:
        t.join()
    print(n)

