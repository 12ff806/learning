#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# class Point
class Point:
    """ define a Point class """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

p = Point(3, 4)
print(p.x, p.y, p.distance_from_origin())
