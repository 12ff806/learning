#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return "Insufficient funds"
        balance = balance - amount
        return balance
    return withdraw

if __name__ == "__main__":
    wd = make_withdraw(20)
    wd2 = make_withdraw(7)
    print(wd2(6))
    print(wd(8))
    print(wd2(1))
    print(wd(2))
    wd3 = wd
    print(wd3(5))

