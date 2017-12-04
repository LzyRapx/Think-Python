#coding:utf-8
from random import *
"""
假如你班上有23个学生，这当中两个人同一天出生的概率是多大？你可以评估一下23个随机
生日中有相同生日的概率。提示一下：你可以用 randint 函数来生成随机的生日，这个函数包
含在 random 模块中。
"""

def has_duplicates(s):
    t = list(s)
    t.sort()

    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            return True
    return False

def gen_birth():
    b1 = [randint(1, 31),  randint(1, 12)]
    b2 = [randint(1, 31),  randint(1, 12)]
    b3 = [randint(1, 31),  randint(1, 12)]
    b4 = [randint(1, 31),  randint(1, 12)]
    b5 = [randint(1, 31),  randint(1, 12)]
    b6 = [randint(1, 31),  randint(1, 12)]
    b7 = [randint(1, 31),  randint(1, 12)]
    b8 = [randint(1, 31),  randint(1, 12)]
    b9 = [randint(1, 31),  randint(1, 12)]
    b10 = [randint(1, 31),  randint(1, 12)]
    b11 = [randint(1, 31),  randint(1, 12)]
    b12 = [randint(1, 31),  randint(1, 12)]
    b13 = [randint(1, 31),  randint(1, 12)]
    b14 = [randint(1, 31),  randint(1, 12)]
    b15 = [randint(1, 31),  randint(1, 12)]
    b16 = [randint(1, 31),  randint(1, 12)]
    b17 = [randint(1, 31),  randint(1, 12)]
    b18 = [randint(1, 31),  randint(1, 12)]
    b19 = [randint(1, 31),  randint(1, 12)]
    b20 = [randint(1, 31),  randint(1, 12)]
    b21 = [randint(1, 31),  randint(1, 12)]
    b22 = [randint(1, 31),  randint(1, 12)]
    b23 = [randint(1, 31),  randint(1, 12)]
    l = [b1, b2, b3, b4, b5, b6, b7, b8, b9,
         b10, b11, b12, b13, b14, b15, b16,
         b17, b18, b19, b20, b21, b22, b23]
    return l

def estimate():
    count = 0
    for i in range(10000):
        if has_duplicates(gen_birth()):
            count += 1
    return count / 100*1.0 / 100.0
    
if __name__=='__main__':
    print estimate()
