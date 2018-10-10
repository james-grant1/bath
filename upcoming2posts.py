# coding: utf-8
""" upcoming2posts
"""
# Originally by Stuart Geiger (@staeiou), MIT license
#
# This is a script you run the day after THW, which changes yesterday's file
# from "upcoming" to "posts" so that the next week's topic shows on the main
# page.


import datetime
from datetime import timedelta
import glob

today = datetime.date.today()
yesterday = today - timedelta(1)

# iso weekday returns 1 for Monday, 7 for Sunday.
if yesterday.isoweekday() == 2:
    yesterday_str = yesterday.strftime("%Y-%m-%d")
    # This will crash below when yesterday was not Tuesday

filename = glob.glob("_posts/" + yesterday_str + "*")[0]

with open(filename, "r") as file:
    file_text = file.read()

file_text = file_text.replace('category: upcoming', 'category: posts')
file_text = file_text.replace('category:upcoming', 'category: posts')

with open(filename, "w") as file:
    file.write(file_text)
