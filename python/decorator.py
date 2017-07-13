#!/usr/bin/python2
# -*- coding: utf-8 -*-

def makeblod(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"

    return wrapped

def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"

    return wrapped

@makeblod
@makeitalic
def hello():
    return "hello world"

print hello()
