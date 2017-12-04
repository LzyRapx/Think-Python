#coding:utf-8


fin = open('C:\Users\LzyRapx\PycharmProjects\untitled\words.txt')

while True:
    word = fin.readline()
    if len(word) > 20:
        print word
    if not word:
        break