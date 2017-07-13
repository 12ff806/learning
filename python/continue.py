#!/usr/bin/env python3
# -*- coding: utf-8 -*-

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)
