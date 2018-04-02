#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import xml.sax

class EventHandler(xml.sax.ContentHandler):
    def __init__(self, target):
        self.target = target
    def startElement(self, name, attrs):
        self.target.send(("start", (name, attrs._attrs)))
    def characters(self, text):
        self.target.send(("text", text))
    def endElement(self, name):
        self.target.send(("end", name))

if __name__ == "__main__":
    from coroutine import coroutine
    
    @coroutine
    def printer():
        while True:
            event = (yield)
            print(event)

    xml.sax.parse("allroutes.xml", EventHandler(printer()))
