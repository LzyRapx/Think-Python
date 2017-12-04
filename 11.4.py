#coding:utf-8
from random import *
import time
import bisect
from bisect import bisect_left
"""
如果你做过了第七章的练习，应该已经写过一个名叫 has_duplicates 的函数了，这个函数用
列表做参数，如果里面有元素出现了重复，就返回真。
用字典来写一个更快速更简单的版本。
"""

fin = open('C:\Users\LzyRapx\PycharmProjects\untitled\words.txt')

def has_duplicates(t):
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False


def has_duplicates2(t):
    return len(set(t)) < len(t)


if __name__ == '__main__':
    t = [1, 2, 3]
    print(has_duplicates(t))#False
    t.append(1)
    print(has_duplicates(t))#True

    t = [1, 2, 3]
    print(has_duplicates2(t))#False
    t.append(1)
    print(has_duplicates2(t))#True
