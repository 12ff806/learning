#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import logging


class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError("invalid value: %s" % s)
    return 10 / n


try:
    foo("0")
except ValueError as e:
    logging.exception(e)
print("END")

