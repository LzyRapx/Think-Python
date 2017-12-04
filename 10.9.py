#coding:utf-8
from random import *
import time
"""
写一个函数，读取文件 words.txt，然后建立一个列表，这个列表中每个元素就是这个文件中
的每个单词。写两个版本的这样的函数，一个使用 append 方法，另外一个用自增运算的模
式：t= t + [x]。看看哪个运行时间更长？为什么会这样？
"""

fin = open('C:\Users\LzyRapx\PycharmProjects\untitled\words.txt')

def create_list(doc):
    l =[]
    while True:
        line = doc.readline()
        l.append(line)
        if not line:
            break
    return l

def create_dict(doc):
    d = {}
    while True:
        line = doc.readline()
        d[line.strip()] =True
        if not line:
            break
    return d
def create_list2(doc):
    l = []
    while True:
        line = doc.readline()
        l = l + [line]
        if not line:
            break
    return l

if __name__=='__main__':
    start = time.clock()
    print create_dict(fin)
    end = time.clock()
    print (end-start),'s'
