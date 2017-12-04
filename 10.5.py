#coding:utf-8

"""
写一个函数，名为 is_sorted，接收一个列表作为参数，如果列表按照字母顺序升序排列，就
返回真，否则返回假。
"""
l = [1, 2, 3, 4]

def is_sorted(L):
    ll = sorted(l)
    return l==ll

if __name__=='__main__':
    print is_sorted(l)
