#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Dict(dict):

    def __init__(self, **kw):
        #dict.__init__(self, **kw)
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


if __name__ == "__main__":
    d = Dict(a=1, b=2)
    print("d =", d)
    print("d[\"a\"] ==", d["a"])
    print("d.a ==", d.a)
    #print("d.c ==", d.c)
    d.name = "Sin"
    print(d.name)
    
    Dict.__setattr__(d, "hobby", "coding")
    d.__setattr__("age", 18)
    print(d.age)
    print(d["age"])
    print(d.hobby)
    print(d["hobby"])
    print(Dict.__getattr__(d, "hobby"))
    print(d.__getattr__("hobby"))
    print("d =", d)

