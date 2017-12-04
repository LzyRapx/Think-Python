#coding:utf-8
from __future__ import print_function, division
import random
import time
import bisect
from bisect import bisect_left
from string import *

"""
写一个程序吧，用集合的减法，来找一下书中包含而列表中不包含的单词吧。
"""

fin = open('C:\Users\LzyRapx\PycharmProjects\untitled\words.txt')
def histogram(s):

    d = {}
    for c in s:
        d[c] = d.setdefault(c, 0) + 1
    return d

hist1 = histogram('abc')
hist2 = histogram('abcd')

hist1 = set(hist1)
hist2 = set(hist2)


print (hist2.difference(hist1))
print (hist1.difference(hist2))
