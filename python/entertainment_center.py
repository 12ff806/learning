#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import fresh_tomatoes
import media


laccordeur = media.Movie("调音师 L'accordeur", "阿德里安（Grégoire Leprince-Ringuet 饰）是一个学习钢琴已有15年之久的天才钢琴家，可是在梦寐以求的伯恩斯坦钢琴大赛上他功败垂成，人生跌落谷底。经过一段时间调整，阿德里安重新振作，成为了一名盲人钢琴调音师。事实上他只是带上了隐形眼镜，这会让别人认为他听觉方面更加敏锐，并由此得到更多的同情和消费，甚至还会窥视到别人的生活与隐私，他兀自沉浸在这种虽处闹市又仿佛置身世外的超然之中。某天，他来到一户人家工作，殊不知这里刚刚发生一起凶案……", "https://img1.doubanio.com/view/photo/raw/public/p1529066859.jpg", "https://www.bilibili.com/video/av1835556")
#print(laccordeur.storyline)
rasputin = media.Movie("Rasputin", "格里高利·叶菲莫维奇·拉斯普京纪录片", "http://i1.hdslb.com/bfs/archive/489c226e033dbcfce55c419e741f764768484033.jpg", "http://www.bilibili.com/video/av11036196")
#print(rasputin.storyline)
#rasputin.show_trailer()

print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)  # Predefined Class Attributes: "__doc__" means the class documentation string.
print(media.Movie.__name__)  # Predefined Class Attributes: "__name__" means the name of the class.
print(media.Movie.__module__)  # Predefined Class Attributes: "__name__" means The name of the module in which this class was defined.
print(media.Movie.__dict__)  # Predefined Class Attributes: "__name__" means The class name space.
print(rasputin.__class__)  # Instance Attributes: "__class__" means The class of this instance.
print(rasputin.__dict__)  # Instance Attributes: "__dict__" means The instance name space.
print(rasputin.VALID_RATINGS)

movies = [laccordeur, rasputin]
fresh_tomatoes.open_movies_page(movies)
