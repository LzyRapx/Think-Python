#coding:utf-8

import time
#print time.time()

def check(a,b,c,n):
    if a**n+b**n==c**n and n>2:
        print("Holy smokes, Fermat was wrong!\n")
        return
    elif n<=2:
        print ("Try to check for numbers n > 2!")
    else:
        print ("No, that doesn't work. Try again\n")


if __name__ == '__main__':
    a,b,c,n = map(int,raw_input().split())

    check(a,b,c,n)
