#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import socket, pickle


class NetConsumer(object):
    def __init__(self, addr):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(addr)
    def send(self, item):
        pitem = pickle.dumps(item)
        self.s.sendall(pitem)
    def close(self):
        self.s.close()

