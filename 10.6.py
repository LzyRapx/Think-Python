#coding:utf-8

"""
两个单词如果可以通过顺序修改来互相转换就互为变位词。写一个函数，名为 is_anagram，
接收两个字符串，如果互为变位词就返回真。
"""

def is_anagram(s1, s2):
    return sorted(list(s1)) == sorted(list(s2))

if __name__=='__main__':
    print(is_anagram('hello', 'eholl'))
