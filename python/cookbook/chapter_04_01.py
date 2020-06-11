#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def manual_iter():
    with open("/etc/passwd") as f:
        try:
            while True:
                line = next(f)
                print(line, end="")
        except StopIteration:
            pass


if __name__ == "__main__":
    manual_iter()
