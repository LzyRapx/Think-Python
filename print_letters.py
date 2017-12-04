#coding:utf-8

from swampy.TurtleWorld import *
from math import *
world = TurtleWorld()
bob = Turtle()
bob.delay =0.001


angle_up = 65
angle_down = angle_up

# Fontsize
size = 30

# New line
def new_line(t):
    pu(t)
    rt(t, 90)
    fd(t, size*1.5)
    rt(t, 90)
    fd(t, size * 8)
    lt(t, 180)
    pd(t)

# the unknown side in an isosceles
c = sqrt(2*(size**2)*(1-cos(radians(180 - (angle_up + angle_down)))))

def space(t, size):
    """
    moves turtle to next starting position for a letter
    t: Respective turtle
    """
    pu(t)
    fd(t, size)
    pd(t)

def turn_space(t, size):
    pu(t)
    lt(t, 180)
    fd(t, size)
    pd(t)


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




def vert(t):
    lt(t, 90)
    fd(t, size)
    lt(t, 180)
    fd(t, size)
    lt(t, 90)

def between(t):
    pu(t)
    fd(t, size/2)
    pd(t)

def top_stroke(t):
    pu(t)
    lt(t, 90)
    fd(t, size)
    rt(t, 90)
    pd(t)
    fd(t, size/2)
    pu(t)
    rt(t, 180)
    fd(t, size/2)
    lt(t, 90)
    fd(t, size)
    lt(t, 90)
    pd(t)

def mid_stroke(t):
    pu(t)
    lt(t, 90)
    fd(t, size/2)
    rt(t, 90)
    pd(t)
    fd(t, size/2)
    pu(t)
    rt(t, 180)
    fd(t, size/2)
    lt(t, 90)
    fd(t, size/2)
    lt(t, 90)
    pd(t)

def bottom_stroke(t):
    fd(t, size/2)
    rt(t, 180)
    fd(t, size/2)
    rt(t, 180)

def down_angle(t):
    rt(t, 90+45)
    fd(t, sqrt((size/2)**2*2))
    rt(t, 180)
    fd(t, sqrt((size/2)**2*2))
    rt(t, 45)


def up_angle(t):
    rt(t, 90-45)
    fd(t, sqrt((size/2)**2*2))
    rt(t, 180)
    fd(t, sqrt((size/2)**2*2))
    rt(t, 45 + 90)

def draw_a(t):
    vert(t)
    top_stroke(t)
    mid_stroke(t)
    between(t)
    vert(t)
    space(t, size/3)

def draw_b(t):
    draw_a(t)
    turn_space(t, size/3)
    fd(t, size/2)
    turn_space(t, size/2)
    space(t, size/3)

def draw_c(t):
    vert(t)
    top_stroke(t)
    bottom_stroke(t)
    space(t, size/2)
    space(t, size/3)

def draw_d(t):
    vert(t)
    top_stroke(t)
    bottom_stroke(t)
    between(t)
    vert(t)
    space(t, size/3)

def draw_e(t):
    draw_c(t)
    turn_space(t, size/3)
    space(t, size/2)
    lt(t, 180)
    mid_stroke(t)
    space(t, size/2)
    space(t, size/3)

def draw_f(t):
    vert(t)
    top_stroke(t)
    mid_stroke(t)
    space(t, size/2)
    space(t, size/3)

def draw_g(t):
    vert(t)
    top_stroke(t)
    bottom_stroke(t)
    between(t)
    lt(t, 90)
    fd(t, size/2)
    lt(t, 90)
    fd(t, size/4)
    lt(t, 180)
    fd(t, size/4)
    rt(t, 90)
    fd(t, size/2)
    lt(t, 90)
    space(t, size/3)

def draw_h(t):
    vert(t)
    mid_stroke(t)
    between(t)
    vert(t)
    space(t, size/3)

def draw_i(t):
    vert(t)
    space(t, size/3)

def draw_j(t):
    top_stroke(t)
    between(t)
    vert(t)
    lt(t, 180)
    fd(t, size/4)
    lt(t, 180)
    fd(t, size/4)
    space(t, size/3)

def draw_k(t):
    vert(t)
    lt(t, 90)
    fd(t, size/2)
    down_angle(t)
    up_angle(t)
    lt(t, 180)
    fd(t, size/2)
    lt(t, 90)
    space(t, size/2)
    space(t, size/3)

def draw_l(t):
    vert(t)
    bottom_stroke(t)
    space(t, size/2)
    space(t, size/3)

def draw_m(t):
    vert(t)
    lt(t, 90)
    fd(t, size)
    down_angle(t)
    lt(t, 180)
    fd(t, size)
    lt(t, 90)
    between(t)
    pu(t)
    lt(t, 90)
    fd(t, size/2)
    pd(t)
    up_angle(t)
    rt(t, 45)
    fd(t, sqrt((size/2)**2*2))
    rt(t, 45 + 90)
    fd(t, size)
    lt(t, 90)
    space(t, size/3)

def draw_n(t):
    lt(t, 90)
    fd(t, size)
    rt(t, 90 + 45)
    fd(t, sqrt((size)**2*2))
    lt(t, 45)
    vert(t)
    space(t, size/3)

def draw_o(t):
    draw_d(t)
    turn_space(t, size/3)
    rt(t, 90)
    fd(t, size)
    rt(t, 90)
    fd(t, size/3)
    lt(t, 180)
    fd(t, size/3)
    lt(t, 90)
    fd(t, size)
    lt(t, 90)
    space(t, size/3)
    space(t, size/3)


def draw_p(t):
    draw_f(t)
    turn_space(t, size/3)
    rt(t, 90)
    pu(t)
    fd(t, size/2)
    pd(t)
    fd(t, size/2)
    pu(t)
    lt(t, 180)
    fd(t, size)
    lt(t, 90)
    space(t, size/3)

def draw_q(t):
    draw_d(t)
    turn_space(t, size/3)
    lt(t, 180)
    fd(t, size/3)
    space(t, size/3)

def draw_r(t):
    draw_f(t)
    turn_space(t, size/3)
    rt(t, 90)
    pu(t)
    fd(t, size/2)
    pd(t)
    fd(t, size/2)
    lt(t, 180)
    fd(t, size/2)
    rt(t, 90)
    fd(t, size/2)
    rt(t, 90)
    down_angle(t)
    lt(t, 180)
    fd(t, size/2)
    lt(t, 90)
    space(t, size/2)
    space(t, size/3)

def draw_s(t):
    bottom_stroke(t)
    mid_stroke(t)
    top_stroke(t)
    pu(t)
    lt(t, 90)
    fd(t, size/2)
    pd(t)
    fd(t, size/2)
    pu(t)
    lt(t, 180)
    fd(t, size)
    lt(t, 90)
    between(t)
    lt(t, 90)
    fd(t, size/2)
    lt(t, 180)
    fd(t, size/2)
    lt(t, 90)
    space(t, size/3)

def draw_t(t):
    top_stroke(t)
    pu(t)
    fd(t, size/2)
    top_stroke(t)
    vert(t)
    space(t, size/2)
    space(t, size/3)

def draw_u(t):
    vert(t)
    bottom_stroke(t)
    between(t)
    vert(t)
    space(t, size/3)

def draw_v(t):
    pu(t)
    lt(t, 90)
    fd(t, size)
    pd(t)
    rt(t, 90 + 45)
    fd(t, sqrt((size)**2*2))
    lt(t, 90)
    fd(t, sqrt((size)**2*2))
    rt(t, 45 + 90)
    pu(t)
    fd(t, size)
    lt(t, 90)
    space(t, size/3)

def draw_w(t):
    pu(t)
    lt(t, 90)
    fd(t, size)
    pd(t)
    rt(t, 90 + 45)
    fd(t, sqrt((size)**2*2))
    lt(t, 90)
    fd(t, sqrt((size/2)**2*2))
    rt(t, 90)
    fd(t, sqrt((size/2)**2*2))
    lt(t, 90)
    fd(t, sqrt((size)**2*2))
    rt(t, 45 + 90)
    pu(t)
    fd(t, size)
    lt(t, 90)
    space(t, size/3)

def draw_x(t):
    lt(t, 45)
    fd(t, sqrt((size)**2*2))
    rt(t, 45 + 90)
    pu(t)
    fd(t, size)
    rt(t, 90 + 45)
    pd(t)
    fd(t, sqrt((size)**2*2))
    lt(t, 180)
    fd(t, sqrt((size)**2*2))
    lt(t, 45)
    space(t, size/3)


def draw_y(t):
    pu(t)
    lt(t, 90)
    fd(t, size)
    pd(t)
    down_angle(t)
    pu(t)
    lt(t, 180)
    fd(t, size)
    lt(t, 90)
    fd(t, size/2)
    lt(t, 90)
    pd(t)
    fd(t, size/2)
    up_angle(t)
    lt(t, 180)
    fd(t, size/2)
    lt(t, 90)
    space(t, size/2)
    space(t, size/3)



def draw_z(t):
    top_stroke(t)
    bottom_stroke(t)
    between(t)
    top_stroke(t)
    bottom_stroke(t)
    turn_space(t, size/2)
    lt(t, 180)
    lt(t, 45)
    fd(t, sqrt((size)**2*2))
    rt(t, 45 + 90)
    pu(t)
    fd(t, size)
    lt(t, 90)
    space(t, size/3)



def alphabet(t):
    draw_a(t)
    draw_b(t)
    draw_c(t)
    draw_d(t)
    draw_e(t)
    draw_f(t)
    draw_g(t)
    draw_h(t)
    draw_i(t)
    draw_j(t)
    new_line(t)
    draw_k(t)
    draw_l(t)
    draw_m(t)
    draw_n(t)
    draw_o(t)
    draw_p(t)
    draw_q(t)
    draw_r(t)
    new_line(t)
    draw_s(t)
    draw_t(t)
    draw_u(t)
    draw_v(t)
    draw_w(t)
    new_line(t)
    draw_x(t)
    draw_y(t)
    draw_z(t)

#alphabet(bob)

def hello(t):
    draw_h(t)
    draw_e(t)
    draw_l(t)
    draw_l(t)
    draw_o(t)

hello(bob)

wait_for_user()
