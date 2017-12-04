#coding:utf-8

from __future__ import print_function, division

def backwards(string):

    index = 1
    while index <= len(string):
        display = string[-index]
        print (display,end="")
        index += 1

#backwards('bundesregierung')

prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        print (letter + 'u' + suffix)
    else:
        print (letter + suffix)

fruit = 'banana'
print (fruit[:])

def find(word, letter, start):

    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1

find("Hello", "e", 0)

def count(word, letter):

    counter = 0
    for i in word:
        if i == letter:
            counter += 1

    print ('the letter', letter, 'is contained', counter, 'times in the word', word)

count('plusquamperfekt', 'p')

word = 'banana'
print (word.count('a'))

