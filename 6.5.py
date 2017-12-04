#coding:utf-8

import math
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(a,a%b)

if __name__ == "__main__":
   print(gcd(5,15))

