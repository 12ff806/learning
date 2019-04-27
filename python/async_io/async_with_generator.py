#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import socket
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ


selector = DefaultSelector()
stopped = False
urls_todo = {'/'}



class Future(object):
    def __init__(self):
        self.result = None
        self._callbacks = []

    def add_done_callback(self, fn):
        self._callbacks.append(fn)

    def set_result(self, result):
        self.result = result
        for fn in self._callbacks:
            fn(self)


class Crawler(object):
    def __init__(self, url):
        self.url = url
        self.response = b''

    def fetch(self):
        
