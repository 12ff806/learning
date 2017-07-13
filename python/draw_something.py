#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import turtle


def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)
    
    some_turtle.right(10)


def draw_flower(some_turtle):
    for i in range(1,37):
        some_turtle.left(10)
        some_turtle.forward(50)
        some_turtle.right(20)
        some_turtle.forward(50)
        some_turtle.right(160)
        some_turtle.forward(50)
        some_turtle.right(20)
        some_turtle.forward(50)


def draw_something():
    window = turtle.Screen()
    window.bgcolor("black")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("red")
    brad.speed(10)
    #
    #for i in range(1,5):
    #    brad.forward(100)
    #    brad.right(90)
    #

    #for i in range(1,37):
    #    draw_square(brad)
    #
    #brad.forward(300)
    
    draw_flower(brad)
    brad.right(90)
    brad.forward(300)
    
    #
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.circle(100)
    #
    #tim = turtle.Turtle()
    #for i in range(1,4):
    #    tim.forward(100)
    #    tim.left(120)
    #

    window.exitonclick()


draw_something()
