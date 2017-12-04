#coding:utf-8

from swampy.TurtleWorld import *
from math import *
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.1


def reg_triangle (t, length): # 三角形
    """
    prints a regular triangle with a certain size
    length: Length of one side
    """
    print t
    for i in range(3):
        fd(t, length)
        lt(t, 180-(180/3))

#reg_triangle(bob, 40)


def triangle(t, length, angle): # 三角形
    """
    prints a triangle with a customizable angle alpha
    t: Turtle
    length: length of side a of triangle
    angle: gamma
    """
    print t
    a = length
    gamma = angle  # angle opposite side c in the triangle
    alpha = (180.0-gamma)/2  # alpha and beta are equal
    c = sqrt(2*(a**2)*(1-cos(radians(gamma))))
    fd(t, a)
    lt(t, 180-alpha)
    fd(t, c)
    lt(t, 180-alpha)
    fd(t, a)
    lt(t, 180)

#triangle(bob, 200, 72)

def pie (t, length, n):
    """
    prints a pie consisting of n isosceles triangles
    t: Turtle to draw the pie
    n: how many triangles
    length: Length of one side of one triangle
    """
    print t
    angle = 360/n
    for i in range(n):
        triangle(bob, length, angle)

#pie(bob, 40, 8)

#pie(bob, 200, 40)

wait_for_user()
