#coding:utf-8
from __future__ import print_function, division
from random import *
import random
import time
import bisect
from bisect import bisect_left
from string import *

"""
写一个程序，用上面说的算法来从一本书中随机挑选单词。
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
                    word = word.strip()
                    word = word.lower()
                    word = word.translate(None, punctuation)
                    word = word.translate(None, whitespace)
                    complete_list.append(word)
    return complete_list

def word_count(l):
    d = {}
    for word in l:
        d[word] = d.setdefault(word, 0) + 1
    return d

worddict = make_worddict(fin)
kamasutra = word_analyzer(fin2)

d = word_count(kamasutra)
#print (d)
#print (len(d))

#cumulative sum of all words in dict as a list
def cum_sum(d):
    res = []
    tmp = 0
    for val in d.values(): #键值
        res.append(tmp + val)
        tmp += val
    return  res

cumsum = cum_sum(d)
n = cumsum[len(cumsum) - 1]
#random number in range from 1 to n, where n is the last item in
rand = randint(1,n)

# Find index, where ran would be inserted into cumsum
def bisect_search(s,num):
    return bisect_left(s,num)
index = bisect_search(cumsum,rand)

# Use index to find corresponding word in wordlist
print (kamasutra[index])
