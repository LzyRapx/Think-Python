#coding:utf-8

from swampy.TurtleWorld import *
from math import *
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

"""
写个程序来画阿基米德曲线（曲线中的一种）
"""

def draw_spiral(t, n, length=3, a=0.01, b=0.0005): #画阿基米德曲线
    """
    Draws an Archimedian spiral starting at the origin.
    参数:
      n:线段的数量
      length: 线段的长度
      a: 大小
      b: 大小
    http://en.wikipedia.org/wiki/Spiral
    """
    theta = 0.0
    for i in range(n):
        fd(t, length)
        dtheta = 1 / (a + b * theta)

        lt(t, dtheta)
        theta += dtheta

draw_spiral(bob, 1000)#1000 = 线段的数量

wait_for_user()
