#coding:utf-8
from __future__ import print_function, division
from random import *
import time
import bisect
from bisect import bisect_left
"""
一个英文单词，每次去掉一个字母，又还是一个正确的英文单词，这是什么词？
然后接下来字母可以从头去掉，也可以从末尾去掉，或者从中间，但不能重新排列其他字
母。每次去掉一个字母，都会的到一个新的英文单词。然后最终会得到一个字母，也还是一
个英文单词，这个单词也能在词典中找到。符合这样要求的单词有多少？最长的是哪个？
给你一个合适的小例子：Sprite。这个词就满足上面的条件。把 r 去掉了是 spite，去掉结尾的
e 是 spit，去掉 s 得到的是 pit，it，然后是 I。
写一个函数找到所有的这样的词，然后找到其中最长的一个。
这个练习比一般的练习难以些，所以下面是一些提示：
1. 你也许需要写一个函数，接收一个单词然后计算一下这个单词去掉一个字母能得到单词
组成的列表。列表中这些单词就如同原始单词的孩子一样。
2. 只要一个 单词的孩子还可以缩减，那这个单词本身就亏缩减。你可以认为空字符串是可
以缩减的，这样来作为一个基准条件。
3. 我上面提供的 words.txt 这个词表，不包含单个字母的单词。所以你需要自行添加 I、a
以及空字符串上去。
4. 要提高程序性能的话，你最好存储住已经算出来能被继续缩减的单词
"""

def make_word_dict():
    """
    Reads a word list and returns a dictionary.
    """
    d = {}#字典
    #d = dict()
    fin = open('C:\Users\LzyRapx\PycharmProjects\untitled\words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = None

    # have to add single letter words to the word list;
    # also, the empty string is considered a word.
    for letter in ['a', 'i', '']:
        d[letter] = letter
    return d

def is_reducible(word, word_dict): #继续减少字母个数

    """
    If word is reducible, returns a list of its reducible children.
    Also adds an entry to the memo dictionary.
    A string is reducible if it has at least one child that is
    reducible.  The empty string is also reducible.
    word: string
    word_dict: dictionary with words as keys
    """
    memo = {}

    """
    memo is a dictionary that maps from each word that is known
    to be reducible to a list of its reducible children.  It starts
    with the empty string.
    """
    memo[''] = ['']
     # if have already checked this word, return the answer
    if word in memo:
         return memo[word]

    # check each of the children and make a list of the reducible ones
    res = [] #列表
    for child in children(word, word_dict):
        if is_reducible(child, word_dict):
            res.append(child)

    # memoize and return the result
    memo[word] = res
    return res


def children(word, word_dict):
    """
    Returns a list of all words that can be formed by removing one letter.
    word: string
    Returns: list of strings
    """
    res = []
    for i in range(len(word)):
        child = word[:i] + word[i+1:] #removing one letter word[i]
        if child in word_dict:
            res.append(child)
    return res


def all_reducible(word_dict):
    """
    Checks all words in the word_dict; returns a list reducible ones.
    word_dict: dictionary with words as keys
    """
    res = []
    for word in word_dict:
        t = is_reducible(word, word_dict)
        if t != []: #不是空的
            res.append(word)
    return res


def print_trail(word):
    """
    Prints the sequence of words that reduces this word to the empty string.
    If there is more than one choice, it chooses the first.
    word: string
    """
    if len(word) == 0:
        return
    print(word, end=' ')
    t = is_reducible(word, word_dict)
    print_trail(t[0])


def print_longest_words(word_dict):
    """
    Finds the longest reducible words and prints them.
    word_dict: dictionary of valid words
    """
    words = all_reducible(word_dict)

    # use DSU to sort by word length
    t = []
    for word in words:
        t.append((len(word), word))
    t.sort(reverse=True)

    # print the longest 5 words
    for _, word in t[0:5]:
        print_trail(word) #打印不断删去一个字母的string
        print('\n')

if __name__ == '__main__':
    
    word_dict = make_word_dict()

    print_longest_words(word_dict)