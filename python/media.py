#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import webbrowser


class Movie():
    # Predefined Class Attributes: "__doc__"
    """ This class provides a way to store movie related information."""

    # Class Variables/Attributes
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # Constructor
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_bilibili):
        # Instance Variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        #self.trailer_bilibili_url = trailer_bilibili
        self.trailer_youtube_url = trailer_bilibili

    def show_trailer(self):
        #webbrowser.open(self.trailer_bilibili_url)
        webbrowser.open(self.trailer_youtube_url)
