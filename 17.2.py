#coding:utf-8

from datetime import *
import dateutil

class Point(object):

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%d,%d)' % (self.x,self.y)

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x, new_y)

point = Point(12,34)

point2 = Point(34,56)

print  point

print point2

print point + point2
