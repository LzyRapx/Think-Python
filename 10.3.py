#coding:utf-8

"""
写一个函数，名为 middle，接收一个列表，返回一个新列表，新列表要求对源列表掐头去尾
只要中间部分。
"""
l = [1, 2, 3, 4]

def middle(l):
    del(l[0])
    l.pop()
    return l


print middle(l)
