#coding:utf-8

"""
写一个名字叫uses_all的函数，接收一个单词和一个必需字母组合的字符串，如果单词对必需
字母组合中的字母至少都用了一次就返回真。有多少单词都用到了所有的元音字母 aeiou？
aeiouy的呢？
"""
def uses_all(word, letters):
    if letters == '':
        return True
    else:
        for char in letters:
            if char in word:
                return uses_all(word, letters.replace(char, ''))
            else:
                return False

# print uses_all('hllo', 'a')


fin = open('C:\Users\LzyRapx\PycharmProjects\untitled\words.txt')
count = 0
while True:
    line = fin.readline()
    if uses_all(line, 'aeiouy'):
        count += 1
        # print line
    if not line:
        break
print count
