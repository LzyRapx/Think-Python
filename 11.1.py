#coding:utf-8
from random import *
import time
import bisect
from bisect import bisect_left
"""
写一个函数来读取 words.txt 文件中的单词，然后作为键存到一个字典中。键值是什么不要
紧。然后用 in 运算符来快速检查一个字符串是否在字典中。
如果你做过第十章的练习，你可以对比一下这种实现和列表中的 in 运算符以及对折搜索的速
度。
"""

fin = open('C:\Users\LzyRapx\PycharmProjects\untitled\words.txt')

def create_list(doc):
    d = []
    while True:
        line = doc.readline()
        d[line.strip()]==True
        if not line:
            break
    return d

def in_bisect(word_list,word):

    i = bisect_left(word_list,word)
    if i != len(word_list) and word_list[i] == word:
        return True
    else:
        return False
my_dictionary = dict()

while True:
    line = fin.readline()
    my_dictionary[line.strip()] = ''
    if not line:
        break

start = time.clock()
print 'asdfg' in my_dictionary
end = time.clock()
print end-start

start = time.clock()
print 'aah' in my_dictionary
end = time.clock()
print end-start


