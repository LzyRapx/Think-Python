#coding:utf-8
from random import *
import time
import bisect
"""
要检查一个单词是不是在上面这个词汇列表里，你可以使用 in 运算符，但可能会很慢，因为
这个 in 运算符要从头到尾来搜索整个词汇表。
我们知道这些单词是按照字母表顺序组织的，所以我们可以加速一下，用一种对折搜索（也
叫做二元搜索），这个过程就和你在现实中用字典来查单词差不多。你在中间部分开始，看
看这个要搜索的词汇是不是在中间位置的前面。如果在前面，就又对前半部分取中间，继续
这样来找。当然了，不在前半部分，就去后半部分找了，思路是这样的。
不论怎样，每次都会把搜索范围缩减到一半。如果词表包含了113809个单词，最多就是17步
就能找到单词，或者能确定单词不在词汇表中。
那么问题来了，写一个函数，名为 in_bisect，接收一个整理过的按照字母顺序排列的列表，
以及一个目标值，在列表中查找这个值，找到了就返回索引位置，找不到就返回空。
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

l = create_list(fin)

def index_search(word, l):
    count = 0
    for i in l:
        if i == word:
            return count
        else:
            count += 1

def make_word_list():
    """
    Reads lines from a file and builds a list using append.
    returns: list of strings
    """
    word_list = []
    fin = open('C:\Users\LzyRapx\PycharmProjects\untitled\words.txt')
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list


def in_bisect(word_list, word):
    """
    Checks whether a word is in a list using bisection search.
    Precondition: the words in the list are sorted
    word_list: list of strings
    word: string
    returns: True if the word is in the list; False otherwise
    """
    if len(word_list) == 0:
        return False

    i = len(word_list) // 2
    if word_list[i] == word:
        return True

    if word_list[i] > word:
        # search the first half
        return in_bisect(word_list[:i], word)

    else:
        # search the second half
        return in_bisect(word_list[i + 1:], word)


def in_bisect_cheat(word_list, word):
    """
    Checks whether a word is in a list using bisection search.
    Precondition: the words in the list are sorted
    word_list: list of strings
    word: string
    """
    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False

    return word_list[i] == word


if __name__ == '__main__':
    word_list = make_word_list()
    print index_search('aah', l) #1
    print index_search('allen', l)#None
    
    for word in ['aah', 'alien', 'allen', 'zymurgyaaa']:
        print(word, 'in list', in_bisect(word_list, word))

    for word in ['aah', 'alien', 'allen', 'zymurgy']:
        print(word, 'in list', in_bisect_cheat(word_list, word))
