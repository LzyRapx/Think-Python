#coding:utf-8
from random import *
import time
import bisect
from bisect import bisect_left
"""
用备忘的方法来改进一下第二章练习中的Ackermann函数，看看是不是能让让函数处理更大
的参数。提示：不行。
"""

fin = open('C:\Users\LzyRapx\PycharmProjects\untitled\words.txt')

cache = {}
def ackermann(m, n):

    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)

    if (m, n) in cache:
        return cache[m, n]
    else:
        cache[m, n] = ackermann(m-1, ackermann(m, n-1))
        return cache[m, n]

print ackermann(3, 6)
print ackermann(3,4)
#print ackermann(5,6)
