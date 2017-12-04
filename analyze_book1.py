from __future__ import print_function, division

import random
import string

"""
process_file这个函数遍历整个文件，逐行读取，
然后把每行的内容发给process_line函数。
词频统计函数 hist 在该程序中是一个累加器。
"""
def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
   
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename)

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        process_line(line, hist)

    return hist


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*END*THE SMALL PRINT!'):
            break
"""
process_line使用字符串的方法 replace把各种连字符都用空格替换，然后用 split 方法把整行
打散成一个字符串列表。程序遍历整个单词列表，然后用 strip 和 lower 这两个方法移除了标
点符号，并且把所有字母都转换成小写的。
"""

def process_line(line, hist):
    """Adds the words in the line to the histogram.

    Modifies hist.

    line: string
    hist: histogram (map from word to frequency)
    """
    # TODO: rewrite using Counter

    # replace hyphens with spaces before splitting
    line = line.replace('-', ' ')
    strippables = string.punctuation + string.whitespace

    for word in line.split():
        # remove punctuation and convert to lowercase
        word = word.strip(strippables)
        word = word.lower()

        # update the histogram
        hist[word] = hist.get(word, 0) + 1

#下面的函数就接收了词频统计结果，然后返回一个『单词-次数』元组组成的列表
def most_common(hist):
    """Makes a list of word-freq pairs in descending order of frequency.

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """
    t = []
    for key, value in hist.items():
        t.append((value, key))

    t.sort()
    t.reverse()
    return t

#这些元组中，要先考虑词频，返回的列表因此根据词频来排序。
#下面是一个输出最常用单词的循环体
def print_most_common(hist, num=10):                `````````````   
    """Prints the most commons words in a histgram and their frequencies.
    
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[:num]:
        print(word, '\t', freq)
#此处用了关键词 sep 来让 print 输出的时候以一个tab跳表符来作为分隔，
#而不是一个空格，这样第二列就会对齐。


def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.

    d1, d2: dictionaries
    """
    # TODO: reimplement using Counter
    res = {}
    for key in d1:
        if key not in d2:
            res[key] = None
    return res

#计算整个文件中的单词总数，就可以把 histogram 中的所有频数加到一起就可以了
def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


#不重复的单词的数目也就是字典中项的个数了
def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)


def random_word(hist):
    """Chooses a random word from a histogram.

    The probability of each word is proportional to its frequency.
    """
    # TODO: rewrite using Counter
    t = []
    for word, freq in hist.items():
        t.extend([word] * freq)

    return random.choice(t)


def main():
    hist = process_file('emma.txt', skip_header=True)
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))

    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[0:20]:
        print(word, '\t', freq)

    words = process_file('words.txt', skip_header=False)

    diff = subtract(hist, words)
    print("The words in the book that aren't in the word list are:")
    for word in diff.keys():
        print(word, end=' ')

    print("\n\nHere are some random words from the book")
    for i in range(100):
        print(random_word(hist), end=' ')


if __name__ == '__main__':
    main()
