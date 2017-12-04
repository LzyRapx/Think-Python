#coding:utf-8
from random import *
import time
import bisect
from bisect import bisect_left

"""
读一下字典中 setdefault 方法的相关文档，然后用这个方法来写一个更精简版本的invert_dict
函数。
"""

fin = open('C:\Users\LzyRapx\PycharmProjects\untitled\words.txt')


def histogram(s):
    d = {}
    for c in s:
        d[c] = 1 + d.get(c,0) #c是键值
    return d

d = histogram('asdfghasdf')
#print  d

def invert_dict(d): #键和键值互换
    invert = {}
    for key,val in d.items():
        invert.setdefault(val,[]).append(key)
    return invert

print invert_dict(d)


