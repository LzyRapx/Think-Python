#coding:utf-8
from random import *
import time
import bisect
from bisect import bisect_left
"""
一个词如果翻转顺序成为另外一个词，这两个词就为『翻转词对』（参见第五章练习的
rotate_word）。
写一个函数读取一个单词表，然后找到所有这样的单词对。
"""
# Rotates a letter by n places.  Does not change other chars.
#注意是一个
def rotate_letter(letter, n):

    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)

# Rotates a word by n places.
def rotate_word(word, n):
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res

fin = open('C:\Users\LzyRapx\PycharmProjects\untitled\words.txt')

def create_dict(doc):
    d = {}
    while True:
        line = doc.readline()
        d[line.strip()] = True
        if not line:
            break
    return d

def find_rotated():
    d = create_dict(fin)
    count = 0
    for word in d:
        for i in range(1, 26): #单词中的全部字母按照某一顺序翻转
            if rotate_word(word, i) in d:
                print word, rotate_word(word, i), i
                count += 1
    print '\n', count

find_rotated()  # 2205
