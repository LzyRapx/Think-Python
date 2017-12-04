#coding:utf-8
from __future__ import print_function, division
import random
import time
import bisect
from bisect import bisect_left
from string import *

"""
写一个名为 choose_from_hist 的函数，用这个函数来处理一下11.2中定义的那个histogram函
数，从histogram 的值当中随机选择一个，这个选择的概率按照比例来定。
"""

fin = open('C:\Users\LzyRapx\PycharmProjects\untitled\words.txt')
def histogram(s):

    d = {}
    for c in s:
        d[c] = d.setdefault(c,0)+1
    return  d

def choose_from_hist(hist):
    l = []
    for key in hist:
        for i in range(hist[key]):
            l.append(key)
    return random.choice(l)

hist = histogram('aacc')

print (choose_from_hist(hist))