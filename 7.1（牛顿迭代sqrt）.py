#coding:utf-8

from math import*

def square_root(a):

    x = a / 4.0
    while True:
        y = (x + a/x) / 2.0
        if abs(y-x) < 0.00000001:
            break
        x = y
    return  x

print square_root(4)
print square_root(6)
