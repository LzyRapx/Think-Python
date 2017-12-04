#coding: utf-8

"""

字母表当中的字母都可以用一定数量的基本元素来构建，比如竖直或者水平的线条，以及一
些曲线。设计一个能用最小数量的基本元素画出来的字母表，然后写个函数来画字母出来。

"""
from swampy.TurtleWorld import *
from math import *
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.001

""" A B C D E F G H I J K L M N O P Q R S T U V W X Y Z """

angle_up = 65
angle_down = angle_up

size = 30 #字体大小

letter_space = 20 #字母相隔距离

# the unknown side in an isosceles
c = sqrt(2*(size**2)*(1-cos(radians(180 - (angle_up + angle_down)))))

def space(t):
    """
    moves turtle to next starting position for a letter
    t: Respective turtle
    """
    pu(t)
    fd(t, letter_space)
    pd(t)

def polyline(t, n, length, angle):
    """
    Draws n line segments.
    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def arc(t, r, angle):
    """
    Draws an arc with the given radius and angle.
    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    lt(t, step_angle/2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle/2)


def draw_a(t, size): #打印字母A
    """
    Draws the capital letter A in a certain size
    t: Turtle to do the job
    size: Font size, to be defined globally
    """
    # draw first leg
    lt(t, angle_up)
    fd(t, size/2)
    # draw triangle
    fd(t, size/2)
    rt(t, 180 - (180 - (angle_up + angle_down)))
    fd(t, size/2)
    rt(t, 180 - angle_up)
    fd(t, c/2)
    # return to adequate position
    rt(t, 180)
    fd(t, c/2)
    # draw second leg
    rt(t, angle_down)
    fd(t, size/2)
    lt(t, angle_up)
    space(t)

draw_a(bob, size)

def draw_b(t, size): #打印字母B
    """
    Draws the capital letter B in a certain size
    t: Turtle to do the job
    size: Font size, to be defined globally
    """
    arc(t, size/4, 180)
    lt(t, 180)
    arc(t, size/4, 180)
    lt(t, 90)
    fd(t, size)
    lt(t, 90)
    pu(t)
    fd(t, size/4)
    pd(t)
    space(t)

draw_b(bob, size)

def draw_c(t, size): #打印字母C

    pu(t)
    fd(t, size/2)
    lt(t, 90)
    fd(t, size)
    lt(t, 90)
    pd(t)
    arc(t, size/2, 180)
    pu(t)
    space(t)

draw_c(bob, size)

def draw_d(t, size): #打印字母D

    arc(t, size/2, 180)
    lt(t, 90)
    fd(t, size)
    lt(t, 90)
    pu(t)
    fd(t, size/2)
    space(t)

draw_d(bob, size)

def draw_e(t,size): #打印字母E

    lt(t, 90)
    fd(t, size)
    rt(t, 90)
    fd(t, size/3)
    rt(t, 180)
    fd(t, size/3)
    lt(t, 90)
    fd(t, size/2)
    lt(t, 90)
    fd(t, size/3)
    rt(t, 180)
    fd(t, size/3)
    lt(t, 90)
    fd(t, size/2)
    lt(t, 90)
    fd(t, size/3)
    space(t)

draw_e(bob, size)

wait_for_user()
