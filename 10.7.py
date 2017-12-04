#coding:utf-8

"""
写一个函数，名为 has_duplicates，接收一个列表，如果里面有重复出现的元素，就返回
真。这个函数不能修改源列表
"""
def has_duplicates(s):
    t = list(s)
    t.sort()

    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            return True
    return False

if __name__=='__main__':
    print(has_duplicates('cba'))
    print(has_duplicates('abba'))
