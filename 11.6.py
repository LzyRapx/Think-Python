#coding:utf-8
from random import *
import time
import bisect
from bisect import bisect_left
"""
这条谜语来自一个名叫 Dan O'Leary的朋友。他最近发现一个单词，这个单词有一个音
节，五个字母，然后有以下所述的特定性质。 去掉第一个字母，得到的是与原词同音异
形异义词，发音与原词一模一样。替换一下首字母，也就是把第一个字母放回去，然后
把第二个字母去掉，得到的是另外一个这样的同音异形异义词。那么问题来了，这是个
什么词呢？
现在我给你提供一个错误的例子。咱们先看一下五个字母的单词，「wrack」。去掉第一
个字母，得到的四个字母单词是「R-A-C-K」。但去掉第二个字母得到的是「W-A-CK」，
这就不是前两个词的同音异形异义词。（译者注：词义的细节就略去了，没有太大
必要。）
但这个词至少有一个，Dan 和咱们都知道的，分别删除前两个字母会产生两个同音异形
异义的四个字母的单词。问题就是，这是哪个词？
字典提供了一个名为read_dictionary的函数，该函数会读取发音词典，然后返回
一个 Python 词典，返回的这个词典会映射每一个单词到描述单词读音的字符串。
写一个函数来找到所有满足谜语要求的单词。

"""

filename = "C:\Users\LzyRapx\PycharmProjects\untitled\c06d.txt"
fin = open('C:\Users\LzyRapx\PycharmProjects\untitled\words.txt')

def read_dictionary(filename):
    """
    Reads from a file and builds a dictionary that maps from
    each word to a string that describes its primary pronunciation.

    Secondary pronunciations are added to the dictionary with
    a number, in parentheses, at the end of the key, so the
    key for the second pronunciation of "abdominal" is "abdominal(2)".

    filename: string
    returns: map from string to pronunciation
    """
    d = dict()
    fin = open(filename)
    for line in fin:
        # skip over the comments
        if line[0] == '#':
            continue

        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron
    return d

def create_dict(doc):
    d = {}
    while True:
        line = doc.readline()
        if len(line.strip()) in range(4,6):
            d[line.strip()] = True
        if not line:
            break
    return d

def new_word(word):
    #del(word[0]) wrong
    return word[1:]

def new_word2(word):
    #del(word[1]) wrong
    return word[0]+word[2:]


def solve():
    for word in word_d:
        word2 = new_word(word)
        word3 = new_word(word)
        if word in pron_d:
            if word2 in pron_d:
                if word3 in pron_d:
                    if pron_d[word] == pron_d[word2]:
                        if pron_d[word] == pron_d[word3]:
                            print word,word2,word3

if __name__ =='__main__':
    word_d = create_dict(fin)
    pron_d = read_dictionary(filename)
    solve()
    
"""
knell nell nell
wrong rong rong
knit nit nit
herb erb erb
wrap rap rap
knead nead nead
knew new new
knee nee nee
hours ours ours
gnash nash nash
eaux aux aux
wraps raps raps
knees nees nees
kneed need need
kneel neel neel
whole hole hole
llama lama lama
scent cent cent
wring ring ring
knoll noll noll
wrung rung rung
extra xtra xtra
write rite rite
gnat nat nat
knots nots nots
wrack rack rack
wreck reck reck
wrath rath rath
aisle isle isle
knave nave nave
hour our our
eide ide ide
gnats nats nats
llano lano lano
knock nock nock
wrest rest rest
eerie erie erie
wrote rote rote
knack nack nack
wrist rist rist
wren ren ren
knot not not
"""
