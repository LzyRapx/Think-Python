#coding:utf-8
from __future__ import print_function, division
from random import *
import time
import bisect
from bisect import bisect_left
from string import *

"""
1.写一个读取文件的程序，把每一行拆分成一个个词，去掉空白和标点符号，然后把所有单词
都转换成小写字母的。
2.修改一下刚才上一个练习你写的程序，让这个程序能读取你下载的这本书，跳过文件开头部
分的信息，继续以上个练习中的方式来处理一下整本书的正文。
然后再修改一下程序，让程序能统计一下整本书的总单词数目，以及每个单词出现的次数。
输出一下这本书中不重复的单词的个数。对比一下不同作者、不同地域的书籍。哪个作者的
词汇量最丰富？
3.再接着修改程序，输出一下每本书中最频繁出现的20个词
4.接着修改，让程序能读取一个单词列表（参考9.1），然后输出一下所有包含在书中，但不包
含于单词列表中的单词。看看这些单词中有多少是排版错误的？有多少是本应被单词列表包
含的常用单词？有多少是很晦涩艰深的罕见词汇.
"""

fin = open('C:\Users\LzyRapx\PycharmProjects\untitled\words.txt')
fin2 = open("C:\Users\LzyRapx\PycharmProjects\untitled\kamasutra.txt")
def make_worddict(doc):
    d = {}
    while True:
        line = doc.readline()
        d[line.strip()] = True
        if not line:
            break
    return d

def word_analyzer(doc):

    complete_list = []
    line = doc.readline()
    for line in doc:
        if 'START OF THIS PROJECT GUTENBERG EBOOK THE KAMA SUTRA OF VATSYAYANA' in line:
            for line in doc:
                l = line.split()
                for word in l:
                    word = word.strip() #去除两侧（不包括内部）空格的字符串，原序列不变
                    word = word.lower() #所有变成小写
                    word = word.translate(None,punctuation)#去掉所有标点
                    word = word.translate(None,whitespace) #去掉所有空白
                    complete_list.append(word)
    return complete_list

def word_count(l):

    d = {}
    for word in l:
        d[word] = d.setdefault(word,0) + 1
    return d

def top_20(d):
    l = []
    top20 = d.values()
    top20.sort(reverse=True)
    for i in range(20):
        l.append(top20[i])
    return l

if __name__ == '__main__':

    worddict = make_worddict(fin)
    kamasutra = word_analyzer(fin2)
    print (len(kamasutra)) #Total number of words in book

    d = word_count(kamasutra)
    print (len(d)) #书中不同的单词个数
    l = top_20(d)

    print (l) # top20
    print ('所有包含在书中，但不包含于单词列表中的单词：')
    count = 0
    no_match_list = []
    for word in kamasutra:
        if word not in worddict and len(word) != 1:
            count += 1
            no_match_list.append(word)

    print ('个数：',len(no_match_list))
    print (no_match_list)

"""
62008
5870
[4660, 3073, 2294, 1631, 1526, 1079, 1031, 1023, 814, 762, 692, 649, 615, 503, 497, 488, 476, 472, 453, 446]
所有包含在书中，但不包含于单词列表中的单词：
个数： 2341
"""


