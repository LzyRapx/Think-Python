#coding:utf-8
from random import *
import random
import time
import math
import bisect
from bisect import bisect_left
import os
import shelve
import matplotlib.pyplot as pyplot
from string import *
#print (os.path.abspath("words.txt"))
"""
写一个名为 Circle 的类的定义，属性为圆心center和半径radius，center 是一个点对象，半径
是一个数值。
实例化一个 Circle 的对象，表示一个圆，圆心在（150，100），半径为75。
写一个名为 point_in_circle 的函数，接收一个 Circle 和一个 Point 对象作为参数，如果点在圆
内或者圆的线上就返回True。
写一个名为 rect_in_circle 的函数，接收一个 Circle 和一个 Rectangle 对象作为参数，如果矩
形的边都内含或者内切在圆内，就返回 True。
写一个名为 rect_circle_overlap 的函数，接收一个 Circle 和一个 Rectangle 对象作为参数，
如果矩形任意一个顶点在圆内就返回 True。或者写个更有挑战性的版本，如果矩形有任意部
分包含在圆内就返回 True。

"""

fin = open('C:\Users\LzyRapx\PycharmProjects\untitled\words.txt')
fin2 = open("C:\Users\LzyRapx\PycharmProjects\untitled\kamasutra.txt")

class Point(object):
    """ Represents a point in 2D space."""

blank = Point()
blank.x = 3.0
blank.y = 4.0

def print_point(p):
    print '(%g,%g)'%(p.x,p.y)

def distance(p1,p2):
    a = abs(p1.x-p2.x)
    b = abs(p1.y-p2.y)
    dis = math.sqrt(a**2 + b**2)
    return  dis

p1 = Point()
p2 = Point()

p1.x = 2.0
p1.y = 1.0

p2.x = 12.0
p2.y = 5.5

print (distance(p1,p2))