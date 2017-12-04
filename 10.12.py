#coding:utf-8
from random import *
import time
import bisect
from bisect import bisect_left
"""
两个单词，依次拼接各自的字母，如果能组成一个新单词，就称之为『互锁』。比如，shoe
和 cold就可以镶嵌在一起组成组成 schooled。
"""

fin = open('C:\Users\LzyRapx\PycharmProjects\untitled\words.txt')

def create_list(doc):
    l = []
    while True:
        line = doc.readline()
        l.append(line.strip())
        if not line:
            break
    return l

def in_bisect(word_list,word):

    i = bisect_left(word_list,word)
    if i != len(word_list) and word_list[i] == word:
        return True
    else:
        return False

def word_smith(word1, word2, n):
    new = word1[n] + word2[n]
    return new

def interlock(word1,word2):

    new = ''
    n = 0
    if len(word1)==len(word2):
        for i in range(len(word1)):
            new = new + word_smith(word1,word2,n)
            n += 1
        return new
    else:
        pass


l = create_list(fin)
for word1 in l:
    for word2 in l:
        res = interlock(word1,word2)
        if in_bisect(l,res):
            print res,word1,word2

