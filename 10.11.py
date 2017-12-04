#coding:utf-8

from random import *
import time
import bisect
"""
两个词如果互为逆序，就称它们是『翻转配对』。写一个函数来找一下在这个词汇表中所有
这样的词对。
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

def is_reverse(word1, word2):
    return word1 == word2[::-1] and word2 == word1[::-1]

def find_all_rev(doc):
    l = create_list(doc)
    for word in l:
        if is_reverse(word,word):
            print word

if __name__ == '__main__':
   find_all_rev(fin)
