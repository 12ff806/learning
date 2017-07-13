#!/usr/bin/env python3
# -*- coding: utf-8 -*-

words = ['cat', 'window', 'defenestrate']
print("words = {}".format(words))

for w in words[:]:
    print(w, len(w))
    if len(w) > 6:
        words.insert(0, w)

print("words = {}".format(words))
