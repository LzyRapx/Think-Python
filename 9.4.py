#coding:utf-8

"""
写一个名叫uses_only的函数，接收一个单词和一个字母字符串，如果单词仅包含该字符串中
的字母，就返回真。你能仅仅用 acefhlo 这几个字母造句子么？或者试试『Hoe alfalfa』?
"""

def uses_only(word,letter):
    for ch in word:
        if ch not in letter:
            return False
    return True

#print uses_only('ace','acefhlo')

def search():
    fin = open('C:\Users\LzyRapx\PycharmProjects\untitled\words.txt')
    while True:
        line = fin.readline()
       # print line
       #  if line == "aah ":
       #      print line
        if uses_only(line,'aahacefhlo'):
            print line
        if not line:
            break
    print "Done"

#search()
if __name__ == '__main__':
    print uses_only('ace', 'acefhlo')
    search()