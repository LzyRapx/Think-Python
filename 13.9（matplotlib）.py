#coding:utf-8
from random import *
import random
import time
import bisect
from bisect import bisect_left
import matplotlib.pyplot as pyplot
from string import *

"""
此如果你将 log f 和 log r 进行二维坐标系投点，就应该得到一条直线，斜率是-s，截距是
log c。
写一个程序，从一个文件中读取文本，统计单词频率，然后每个单词一行来输出，按照词频
的降序，同时输出一下 log f 和 log r。
选一种投图程序，把结果进行投图，然后检查一下是否为一条直线。
能否估计一下 s 的值呢？
"""

fin = open('C:\Users\LzyRapx\PycharmProjects\untitled\words.txt')
fin2 = open("C:\Users\LzyRapx\PycharmProjects\untitled\kamasutra.txt")
def read_text(doc):
    """
    Reads a text and outputs a histogram of words in form of a
    dictionary where keys: word and values: frequency
    """
    histogram = {}
    line = doc.readline()
    for line in doc:
        words = line.split()
        for word in words:

            word = word.lower()
            word = word.strip()
            word = word.translate(None, punctuation)
            word = ''.join(i for i in word if not word.isdigit())
            histogram[word] = histogram.get(word, 0) + 1

    return histogram

hist = read_text(fin2)

l = []
for freq in hist.values():
    l.append(freq)
    l.sort(reverse=True)

rankdata = []
freqdata = []

for i in range(len(l)):

    rank = i+1
    rankdata.append(rank)

    freq = l[i]
    freqdata.append(freq)


pyplot.plot(rankdata, freqdata)
pyplot.xscale('log') #排名
pyplot.yscale('log') #词频
pyplot.show()
