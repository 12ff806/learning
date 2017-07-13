#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import urllib.request


def read_text():
    quotes = open("/home/sins/Downloads/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)


def check_profanity(text_to_check):
    #connection = urllib.request.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    connection = urllib.request.urlopen("https://12ff806.github.io")
    output = connection.read()
    print(output)
    connection.close()


read_text()
