#coding:utf-8

from math import*

def eval_loop():

    res = 0
    while True:
        line = input()
        if line == 'done':
            break
        else:
            res = res + eval(line)
    return res

if  __name__ == '__main__':
    print  eval('1 + 2 * 3')
    print eval_loop()