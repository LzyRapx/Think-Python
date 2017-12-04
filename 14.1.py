#coding:utf-8
from random import *
import random
import time
import bisect
from bisect import bisect_left
import os
import matplotlib.pyplot as pyplot
from string import *
print (os.path.abspath("words.txt"))
"""
写一个函数，名为 sed，接收一个目标字符串，一个替换字符串，然后两个文件名；读取第一
个文件，然后把内容写入到第二个文件中，如果第二个文件不存在，就创建一个。如果目标
字符串在文件中出现了，就用替换字符串把它替换掉。
如果在打开、读取、写入或者关闭文件的时候发生了错误了，你的程序应该要捕获异常，然
后输出错误信息，然后再退出。
"""

fin = open('C:\Users\LzyRapx\PycharmProjects\untitled\words.txt')
fin2 = open("C:\Users\LzyRapx\PycharmProjects\untitled\kamasutra.txt")

def sed(pattern,sreplace,file1,file2):

    try:
        path_file1 = os.path.abspath(file1)
        read = open(path_file1,'r')
        write = open(file2,'w')
        while True:
            line = read.readline()
            line = line.replace(pattern,sreplace)
            write.write(line)
            if not line:
                break
        read.close()
        write.close()
    except:
        print ("发生错误")

sed('www.spam.de', 'www.kein-spam.de', 'C:\Users\LzyRapx\PycharmProjects\untitled\some-text-source', 'new.txt')
