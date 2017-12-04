#coding:utf-8
from random import *
import time
import bisect
from bisect import bisect_left
"""
更多变位词了！
1. 写一个函数，读取一个文件中的一个单词列表（参考9.1），然后输出所有的变位词。
下面是可能的输出样式的示范：
['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled'] ['retainers', 'ternaries']
['generating','greatening'] ['resmelts', 'smelters', 'termless']
提示：你也许可以建立一个字典，映射一个特定的字母组合到一个单词列表，单词列表中的
单词可以用这些字母来拼写出来。那么问题来了，如何去表示这个字母的集合，才能让这个
集合能用作字典的一个键？
2.修改一下之前的程序，让它先输出变位词列表中最长的，然后是其次长的，依此类推。
1. 在拼字游戏中，当你已经有七个字母的时候，再添加一个字母就能组成一个八个字母的
单词，这就 TMD『bingo』 了（什么鬼东西？老外拼字游戏就跟狗一样，翻着恶心死
了）。然后哪八个字母组合起来最可能得到 bingo？提示：有七个。（简直就是狗一样的
题目，麻烦死了，这里数据结构大家学会了就好了。）

"""

fin = open('C:\Users\LzyRapx\PycharmProjects\untitled\words.txt')

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

def print_anagram_sets(d):
    """
    Prints the anagram sets in d.
    d: map from words to list of their anagrams
    """
    for v in d.values():
        if len(v) > 1:
            print(len(v), v)

def print_anagram_sets_in_order(d):
    """
    Prints the anagram sets in d in decreasing order of size.
    d: map from words to list of their anagrams
    """
    # make a list of (length, word pairs)
    t = []
    for v in d.values():
        if len(v) > 1:
            t.append((len(v), v))

    # sort in ascending order of length
    t.sort()

    # print the sorted list
    for x in t:
        print(x)

def filter_length(d, n):
    """
    Select only the words in d that have n letters.
    d: map from word to list of anagrams
    n: integer number of letters
    returns: new map from word to list of anagrams
    """
    res = {}
    for word, anagrams in d.items():
        if len(word) == n:
            res[word] = anagrams
    return res


if __name__ == '__main__':

    anagram_map = all_anagrams('C:\Users\LzyRapx\PycharmProjects\untitled\words.txt')
    print_anagram_sets_in_order(anagram_map)

    eight_letters = filter_length(anagram_map, 8)
    print_anagram_sets_in_order(eight_letters)