#!/usr/bin/python
# -*- coding: utf-8 -*-

my_name = "Janus Zhao"
my_age = 22 # not a lie
my_height = 67.7165 # inches
my_weight = 121.2542 # lbs
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %s." % my_name
print "He's %f inches tall." % my_height
print "He's %f pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %f, and %f I get %f." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
