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

import copy

class Point(object):
    """Represents a point in 2D space."""


class Rectangle(object):
    """
    Represents a rectangle in 2D space.
    Attributes: width, height, corner
    """


def grow_rectangle(rect, dx, dy):
    """
    Takes a rectangle and moves its left corner to new coordinates dx and dy.
    """
    rect2 = copy.deepcopy(rect)
    rect2.corner.x += dx
    rect2.corner.y += dy
    return rect2


box = Rectangle()
box.width = 100
box.height = 50

box.corner = Point()
box.corner.x = 5
box.corner.y = 2

print box.corner.x
print box.corner.y

grow_rectangle(box, 50, 40)

print box.corner.x
print box.corner.y

d = grow_rectangle(box, 55, 40)

print d.corner.x
print d.corner.y
