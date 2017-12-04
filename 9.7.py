#coding:utf-8

"""
给我一个有三个连续双字母的单词。我会给你一对基本符合的单词，但并不符合。例如，
committee 这个单词，C O M M I T E。如果不是有单独的一个 i 在里面，就基本完美了，或
者Mississippi 这个词：M I S I S I P I。如果把这些个 i 都去掉就好了。但有一个词正好
是三个重叠字母，而且据我所知这个词可能是唯一一个这样的词。当然有有可能这种单词
有五百多个呢，但我只能想到一个。是哪个词呢？写个程序来找一下这个词吧
"""

def three_consecutives(word):
    while True:
        if len(word) < 6:
            return False
        if word[0]==word[1]:
            if word[2]==word[3]:
                if word[4]==word[5]:
                    return  True
                else:
                    return three_consecutives(word[5:])
            else:
                return three_consecutives(word[3:])
        else:
            return three_consecutives(word[1:])

def solve():
 cnt = 0
 fin = open('C:\Users\LzyRapx\PycharmProjects\untitled\words.txt')
 while True:
     line = fin.readline()
     if three_consecutives(line):
         print line
     if not line:
         break

if __name__ =='__main__':
    print  solve()
