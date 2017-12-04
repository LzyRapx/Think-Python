#coding:utf-8

from __future__ import print_function, division
from swampy.TurtleWorld import *
import turtle

"""
写一个叫做snowflake的函数，画三个Koch曲线来制作一个雪花的轮廓。
"""
def koch(t, n):
    """
    Draws a koch curve with length n.
    """
    if n < 10:
        t.fd(n)
        return
    m = n/3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)


def snowflake(t, n):
    """
    Draws a snowflake (a triangle with a Koch curve for each side).
    """
    for i in range(3):
        koch(t, n)
        t.rt(120)


bob = turtle.Turtle()

bob.pu()
bob.goto(-150, 90)
bob.pd()
snowflake(bob, 300)

turtle.mainloop()
wait_for_user()