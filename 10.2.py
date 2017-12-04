#coding:utf-8

"""
写一个函数，明切 cumsum，接收一个数字列表，然后返回累加的总和；也就是新列表的第 i
个元素就是源列表中前 i+1个元素的累加。
"""
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def cum_sum(l):
    res = []
    prev = 0
    i = 1
    for i in l:
        res.append(prev+i)
        prev += i
    return res


print cum_sum(l)
