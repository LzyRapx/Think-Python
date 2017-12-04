#coding:utf-8
from random import *
import random
import time
import bisect
from bisect import bisect_left
import os
import shelve
import matplotlib.pyplot as pyplot
from string import *
print (os.path.abspath("words.txt"))

"""
写一个模块，导入 anagram_sets 然后提供两个函数：store_anagrams 可以把相同字母异序
词词典存储到一个『shelf』；read_anagrams 可以查找一个词，返回一个由其相同字母异序
词 组成的列表。
"""

fin = open('C:\Users\LzyRapx\PycharmProjects\untitled\words.txt')
fin2 = open("C:\Users\LzyRapx\PycharmProjects\untitled\kamasutra.txt")

def signature(s):
    """
    Returns the signature of this string.
    Signature is a string that contains all of the letters in order.
    s: string
    """
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t

def all_anagrams(filename):
    """
    Finds all anagrams in a list of words.
    filename: string filename of the word list
    Returns: a map from each word to a list of its anagrams.
    """
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)

        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d

def store_anagrams(d):
    db = shelve.open('anagram_database.db')
    for key, value in d.items():
        db[key] = value
    db.close()

def read_anagrams(word):
    db = shelve.open('anagram_database.db')
    word = signature(word)
    try:
        return db[word]
    except:
        return []

d = all_anagrams('words.txt')
store_anagrams(d)
print read_anagrams('post')
