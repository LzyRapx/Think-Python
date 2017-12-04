#coding:utf-8

from swampy.TurtleWorld import *
from math import *
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01



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

#polyline(bob, 60, 30, 45)

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

def petal(t, r, angle):
    """
    Draws a petal using two arcs.
    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(2):
        arc(t, r, angle)
        lt(t, 180-angle)

#petal(bob, 200, 70)

def flowers(t, n, size, angle): #t = bob
    """
    打印 n 朵叶子的花
    t: turtle
    n: How many lea
    size: How big the flower
    """
    print t
    for i in range(n):
        petal(t, size, angle)
        lt(t, 360/n)

flowers(bob, 8, 150, 70)

wait_for_user()
