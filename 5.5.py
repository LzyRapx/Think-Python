#coding:utf-8

from swampy.TurtleWorld import *
from math import *
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.1 #delay太大( >=10 )直接卡死，画图的快慢程度


def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    fd(t, length*n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)


draw(bob, 40, 2)
wait_for_user()
