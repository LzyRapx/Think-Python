#coding:utf-8
from random import *
import random
import time
import bisect
from bisect import bisect_left
from string import *

"""
写一个程序，用上面说的算法(Markov analysis 马科夫分析)来从一本书中随机挑选单词。
"""

fin = open('C:\Users\LzyRapx\PycharmProjects\untitled\words.txt')
fin2 = open("C:\Users\LzyRapx\PycharmProjects\untitled\kamasutra.txt")
from random import *

from string import *

def text_reader(doc):
    """
    Reads a document and returns it as a list of all words included
    The list is ordered in the same way that the text was
    """
    doc = doc.read().decode("utf-8-sig").encode("utf-8")
    doc = doc.lower()
    doc = doc.strip()
    doc = doc.translate(None, punctuation)
    return doc.split()


def get_prefixes(l, prefix=2):
    """
    Takes a list of words in text-based order and forms a dictionary with
    keys as tuples of prefixes ... values are lists of single word suffixes
    that can follow the tuple of prefixes
    (...prefixes can have multiple words)
    """
    for index in range(len(l)):
        key_tuple = l[index]
        for i in range(prefix-1):
            if index < len(l) - prefix:
                key_tuple += ' ' + l[index + (i+1)]
                d[tuple(key_tuple.split())] = \
                    d.get(tuple(key_tuple.split()), []) \
                    + [l[index + prefix]]


def generate_text(d, how_many_lines=5):
    """
    Takes a dictionary as input where keys (tuples of prefixes) map to
    values (list of words that follow after the prefixes = suffixes).
    The dictionary was created using markov analysis.
    Using the dictionary, this function picks a prefix at random and maps
    them to a suffix picked at random.
    In the following, the last words of the existing text is taken as a
    prefix to pick a new suffix at random.
    """
    # prefix_len is determined by dictionary
    prefix_len = len(choice(d.keys()))
    # Pick the beginning of random text
    start = choice(d.keys())
    for i in range(len(start)):
        print (start[i])
    # Initiate counter to stop after a number of lines (5 by default)
    lines = 0
    poem = []
    while lines <= how_many_lines:
        output = ''
        for i in range(prefix_len):
            output += ' ' + start[i]
        suffix = choice(d[start])
        output += ' ' + suffix
        poem.append([output])
        next_pick_list = output.split()
        start = tuple(next_pick_list[len(next_pick_list)
                      - prefix_len:len(next_pick_list)])
        lines += 1
    # print poem
    for l in poem:
        delimiter = ' '
        l = delimiter.join(l).split()
        word = l[len(l)-1:]
        print (word[0])

# Text of a document as a list of all its words
kamasutra = text_reader(fin2)


# Dictionary that contains tuples of prefixes as keys and a list
# of possible suffixes as values
d = {}

# Builds a dictionary with all possible prefixes and their one-word suffix
# Length of prefixes is customizable and 2 if not specified
get_prefixes(kamasutra, 4)

# Write poem
generate_text(d, 25)
