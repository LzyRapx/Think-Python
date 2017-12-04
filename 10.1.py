#coding:utf-8

"""
写一个函数，名为 nested_sum，接收一系列的整数列表，然后把所有分支列表中的元素加起
来。
"""

array=[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [20]]

def nested_sum(list):
    cnt = 0;
    for i in range(3):
        cnt += sum(array[i])
        return cnt

print nested_sum(array)