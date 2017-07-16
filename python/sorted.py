#!/usr/bin/env python3
# -*- coding: utf-8 -*-


L = [("Bob", 75), ("Adam", 92), ("bart", 66), ("Lisa", 88), ("morry", 99)]


def by_name(t):
    return t[0].lower()


def by_score(t):
    return t[1]


L1 = sorted(L, key=by_name)
L2 = sorted(L, key=by_score, reverse=True)
print(L1)
print(L2)
