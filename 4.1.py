#coding:utf-8

from math import *
from swampy.TurtleWorld import *

def square(t, length):
    """
    Draws a square with sides of the given length.
    Returns the Turtle to the starting position and location.
    t: Turtle
    length: Side length of square
    """
    for i in range(4):
        fd(t, length)
        lt(t)

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

world = TurtleWorld()
ray = Turtle()
# polyline(ray, 5, 50, 125)

def polygon(t, n, length):
    """
    Draws a regular polygon with n sides.
    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)

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

ray.delay = 0.01
arc(ray, 20, 270)
wait_for_user()

def circle(t, r):
    """
    Draws a circle with the given radius.
    t: Turtle
    r: radius
    """
    arc(t, r, 360)

if __name__ == '__main__':

    world = TurtleWorld()
    bob = Turtle()
    bob.delay = 0.001


    radius = 80 #圆的半径
    
    #打印第一个大半圆
    pu(bob)
    fd(bob, radius)
    lt(bob)
    pd(bob)

    circle(bob, radius) #第二个完整的圆

    wait_for_user()

