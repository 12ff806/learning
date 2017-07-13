#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import webbrowser
import time

break_time = 0
total_times = 3

print("Start time: " + time.ctime())
while(break_time < total_times):
    time.sleep(30)
    webbrowser.open("http://www.luoo.net/essay/344")
    break_time = break_time + 1
