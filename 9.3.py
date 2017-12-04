#coding:utf-8

"""
写一个名叫 avoids 的函数，接收一个单词和一个禁用字母组合的字符串，如果单词不含有该
字符串中的任何字母，就返回真。 修改一下程序代码，提示用户输入一个禁用字母组合的字
符串，然后输入不含有这些字母的单词数目。你能找到5个被禁用字母组合，排除单词数最少
吗？
"""

def avoids(word,forbidden):
    word = word.lower()
    forbidden  = forbidden.lower()
    for ch in word:
        for letter in forbidden:
            if letter == ch:
                return False
    return True

alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in range(5):
    highscore = 0
    for i in alphabet:
        cnt = 0
        forbidden = i
        fin = open('C:\Users\LzyRapx\PycharmProjects\untitled\words.txt')
        while True:
            line = fin.readline()
            if avoids(line,forbidden):
                cnt+=1
            if not line:
                break
        if cnt > highscore:
            best = i
            highscore = cnt

    alphabet = alphabet.replace(best,'')
    print best, #q j x z w