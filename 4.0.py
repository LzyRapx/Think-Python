#coding:utf-8

"""

1.写一个函数叫做square（译者注：就是正方形的意思），有一个名叫t的参数，这个t是一个
turtle。用这个turtle来画一个正方形。写一个函数调用，把bob作为参数传递给square，然后
再运行这个程序。

2.给这个square函数再加一个参数，叫做length（译者注：长度）。把函数体修改一下，让长
度length赋值给各个边的长度，然后修改一下调用函数的代码，再提供一个这个对应长度的参
数。再次运行一下，用一系列不同的长度值来测试一下你的程序。

3.复制一下square这个函数，把名字改成polygon（译者注：意思为多边形）。另外添加一个
参数叫做n，然后修改函数体，让函数实现画一个正n边的多边形。提示：正n多边形的外角为
360/n度。

4.在写一个叫做circle（译者注：圆）的函数，也用一个turtle类的对象t，以及一个半径r，作
为参数，画一个近似的圆，通过调用polygon函数来近似实现，用适当的边长和边数。用不同
的半径值来测试一下你的函数。
提示：算出圆的周长，确保边长乘以边数的值（近似）等于圆周长。

5.在circle基础上做一个叫做arc的函数，在circle的基础上添加一个angle（译者注：角度）变
量，用这个角度值来确定画多大的一个圆弧。用度做单位，当angle等于360度的时候，arc函
数就应当画出一个整团了。

"""
from swampy.TurtleWorld import *
from math import *
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def squre(t,length): #正方形
    print t
    for i in range(4):
        fd(t,length)
        lt(t)
    wait_for_user()

#squre(bob,30)

def polygon(t,length,n):#正n边形
    print t
    angle = 360.0/n
    for i in range(n):
        fd(t,length)
        lt(t,angle)
    wait_for_user()

#polygon(bob,50,6)

def circle(t,r): # 圆
    print t
    circumference = pi * 2 * r
    n = int((circumference/3)+1)
    #n = 360
    length = circumference / n
    polygon(t,length,n) #圆可以看成边数巨大的正多边形
    wait_for_user()

#circle(bob,50)

def arc(t,r,angle): #弧度
    arc_length = pi * 2 * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    for i in range(n):
        fd(t,step_length)
        lt(t,step_angle)
    wait_for_user()

arc(bob,50,90)



