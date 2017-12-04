#coding:utf-8

"""
写一个名字叫is_abecedarian的函数，如果单词中所有字母都是按照字母表顺序出现就返回真
（重叠字母也是允许的）。有多少这样的单词？
"""

def is_abecedarian(word):
    index = 0
    Length = len(word)-1
    for i in range(Length):
        if ord(word[index]) <= ord(word[index+1]):
            index += 1
        else:
            return False
    return True
print is_abecedarian("aab")

def solve():
 cnt = 0
 fin = open('C:\Users\LzyRapx\PycharmProjects\untitled\words.txt')
 while True:
     line = fin.readline()
     if is_abecedarian(line)==True:
         cnt += 1
         print line
     if not line:
         break
 return cnt

if __name__ =='__main__':
    print  solve()
