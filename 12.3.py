#coding:utf-8
from random import *
import time
import bisect
from bisect import bisect_left
"""
两个单词，如果其中一个通过调换两个字母位置就能成为另外一个，就成了一个『交换
对』。协议额函数来找到词典中所有的这样的交换对。提示：不用测试所有的词对，不用测
试所有可能的替换方案。

"""
fin = open('C:\Users\LzyRapx\PycharmProjects\untitled\words.txt')

def metathesis(s1,s2):

    d0 = {}
    d1 = {}
    count = 0
    for key, char in enumerate(s1):
        d0[key] = char
    for key, char in enumerate(s2):
        d1[key] = char

    for key in d0:
        if d0[key] != d1[key]:
            count += 1
            if count > 2: #超过2个字母不一样
                return False
    return True

def tuple_list(s):
    """
    Takes a string and returns a sorted tuple of all its letters
    """
    s = s.strip()#移除s中的空格
    s = list(s)
    s.sort()
    return tuple(s)

def print_anagram_lists(doc, x, y):
    """
    Returns a dictionary containing tuples of letters as keys and all
    anagrams that can be formed out of these letters in form as a list as
    values
    doc: List of words
    x, y: Providing a range for which length the anagram lists shoud have
    """
    d = {} #字典，相当c++的map
    while True:
        line = doc.readline()
        d[tuple_list(line)] = d.get(tuple_list(line), []) + [line.strip()]
        if not line:
            break
    d2 = {}
    for key in d:
        if len(d[key]) in range(x, y):#键值大小在[x,y)之间
            d2[key] = d[key]
    return d2

def all_metatheses(d):
    """
    Takes a dictionary that contains anagrams as values and returns a
    dictionary that maps each anagram to its metathesis if it has one.
    """
    res = {}
    for key in d: #键
        for word0 in d[key]: #键值 = string
            for word1 in d[key]: #键值 = string
                if metathesis(word0, word1) and word0 != word1:
                    print word0,word1
                    res.setdefault(word0, word1)
    return res

if __name__ == '__main__':
    all_anagrams = print_anagram_lists(fin,2,20)

    res = all_metatheses(all_anagrams)
   # print res
