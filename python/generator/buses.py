#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from coroutine import coroutine

@coroutine
def buses_to_dicts(target):
    while True:
        event, value = (yield)
        if event == "start" and value[0] == "bus":
            busdict = {}
            fragments = []
            while True:
                event, value = (yield)
                if event == "start":
                    fragments = []
                elif event == "text":
                    fragments.append(value)
                elif event == "end":
                    if value != "bus":
                        busdict[value] = "".join(fragments)
                    else:
                        target.send(busdict)
                        break

@coroutine
def filter_on_field(fieldname, value, target):
    while True:
        bd = (yield)
        if bd.get(fieldname) == value:
            target.send(bd)

@coroutine
def bus_location():
    while True:
        bus = (yield)
        print("%(route)s, %(id)s, \"%(direction)s\", %(latitude)s, %(longitude)s" % bus)

if __name__ == "__main__":
    from cosax import EventHandler
    import xml.sax

    xml.sax.parse("allroutes.xml", EventHandler(buses_to_dicts(filter_on_field("route", "22", filter_on_field("direction", "North Bound", bus_location())))))
    

