#coding:utf-8

def is_palindrome(i,start,length):
    s = str(i)[start:start+length]
    return s == s[::-1]

def check(i):
    return is_palindrome(i,2,4) and is_palindrome(i+1,1,5)\
            and  is_palindrome(i+2,1,4) and is_palindrome(i+3,0,6)
def solve():
 i = 100000
 while i<=999999:
     if check(i):
         print i
     i=i+1

if __name__ =='__main__':
    print  solve()
