#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from coprocess import recvfrom
from buses import *

# 这里和python2不一样，python2只要传递sys.stdin就可以了
recvfrom(sys.stdin.buffer, filter_on_field("route", "22", filter_on_field("direction", "North Bound", bus_location())))
