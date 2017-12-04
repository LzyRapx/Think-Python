#coding:utf-8

from datetime import *
import dateutil

class Point(object):

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%d,%d)' % (self.x,self.y)

    def add_point(self,other):
       new_x = self.x + other.x
       new_y = self.y + other.y
       return Point(new_x,new_y)

    def add_tuple(self,t):
        new_x = self.x + t[0]
        new_y = self.y + t[1]
       # new_z = self.z + t[2]
       # return Point(new_x,new_y,new_z)
        return Point(new_x,new_y)

    def __add__(self, other):
        if isinstance(other,Point):
            return self.add_point(other)
        else:
            return self.add_tuple(other)

point = Point(34,56)

point2 = Point(67,89)

T = (1,3,4)

t = (23,45,1)

t1 = (1,2,3)

print point + point2

print point2 + T

print t1 + t

