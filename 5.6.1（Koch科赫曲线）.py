#coding:utf-8

from swampy.TurtleWorld import *
from math import *
world = TurtleWorld()
bob = Turtle()
bob.delay = .0001

"""
写一个叫做koch的函数，用一个小乌龟turtle以及一个长度length做形式参数，用这个小
乌龟来画给定长度length的Koch曲线.

"""
def koch(t, n):
    """
    Draws a koch curve with length n.
    """
    if n < 3:
        fd(t, n)
        return
    m = n/3.0
    koch(t, m)
    lt(t, 60)
    koch(t, m)
    rt(t, 120)
    koch(t, m)
    lt(t, 60)
    koch(t, m)


def snowflake(t, n):
    for i in range(3):
        koch(bob, n)
        rt(bob, 180-60)


def quad_koch(t, n):
    """
    Draws the quadratic type 1 variant of a koch curve with length n.
    """
    if n < 4:
        fd(t, n)
        return
    m = n/4.0
    koch(t, m)
    lt(t, 90)
    koch(t, m)
    rt(t, 90)
    koch(t, m)
    rt(t, 90)
    koch(t, m)
    lt(t, 90)
    koch(t, m)

quad_koch(bob, 100)
rt(bob, 90)
quad_koch(bob, 100)
rt(bob, 90)
quad_koch(bob, 100)
rt(bob, 90)
quad_koch(bob, 100)

wait_for_user()
