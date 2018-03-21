#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Sin"

"""
Design pattern: Singleton
"""


import threading
import time


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class Bus(Singleton):
    lock = threading.RLock()
    
    def sendData(self, data):
        self.lock.acquire()
        time.sleep(3)
        print("Sending Signal Data: %s ..." % data)
        self.lock.release()


class VisitEntity(threading.Thread):
    my_bus = ""
    name = ""

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def run(self):
        self.my_bus = Bus()
        self.my_bus.sendData(self.name)


if __name__ == "__main__":
    for i in range(3):
        print("Entity %d begin to run ..." % i)
        my_entity = VisitEntity()
        my_entity.setName("Entity_%d" % i)
        my_entity.start()

