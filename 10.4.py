#coding:utf-8

"""
写一个函数，名为 chop，接收一个列表，修改这个列表，掐头去尾，返回空值。
"""
l = [1, 2, 3, 4]

def chop(l):
    del(l[0])
    del(l[len(l)-1])

if __name__=='__main__':
    chop(l)
    print l
