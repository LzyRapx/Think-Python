#coding:utf-8
from random import *
import time
import bisect
from bisect import bisect_left
"""
写一个名为most_frequent的函数，接收一个字符串，然后用出现频率降序来打印输出字母。
找一些不同语言的文本素材，然后看看不同语言情况下字母的频率变化多大。然后用你的结
果与这里[https://en.wikipedia.org/wiki/Letter_frequency]的数据进行对比。

"""

def most_frequent(s):

    s = s.lower()
    d = {}
    for letter in s:
        if letter in d:
            d[letter] += 1
        else:
            #典 setdefault() 函数和get() 方法类似
            #  如果键不存在于字典中，将会添加键并将值设为默认值。
            #dict.setdefault(key, default=None)
            d.setdefault(letter,1)

    l = []
    for letter,ocurrence in d.items():
        t = ocurrence,letter
        l.append(t)

    l.sort(reverse=True)

    for ocurrence,letter in l:
        print letter,ocurrence

s = open('C:\Users\LzyRapx\PycharmProjects\untitled\words.txt').read()

if __name__ =='__main__':
    most_frequent(s)

