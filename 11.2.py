#coding:utf-8
from random import *
import time
import bisect
from bisect import bisect_left

"""
��һ���ֵ��� setdefault ����������ĵ���Ȼ�������������дһ��������汾��invert_dict
������
"""

fin = open('C:\Users\LzyRapx\PycharmProjects\untitled\words.txt')


def histogram(s):
    d = {}
    for c in s:
        d[c] = 1 + d.get(c,0) #c�Ǽ�ֵ
    return d

d = histogram('asdfghasdf')
#print  d

def invert_dict(d): #���ͼ�ֵ����
    invert = {}
    for key,val in d.items():
        invert.setdefault(val,[]).append(key)
    return invert

print invert_dict(d)


