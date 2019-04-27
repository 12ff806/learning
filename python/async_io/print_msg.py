#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time
from datetime import datetime


def print_message_periodical(interval_seconds, message="keep alive"):
    while True:
        print("{} - {}".format(datetime.now(), message))
        start = time.time()
        end = start + interval_seconds
        while True:
            yield
            now = time.time()
            if now >= end:
                break


if __name__ == "__main__":
    a = print_message_periodical(3, "hello")
    b = print_message_periodical(5, "world")
    stack = [a, b]
    while True:
        for task in stack:
            next(task)

