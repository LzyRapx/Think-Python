#coding:utf-8

def is_triangle(a,b,c):

    if a+b<c or a+c<b or b+c<a:
        print ("No, this cannot be a triangle.")
    else:
        print ("Yes, this would be a triangle.")

if __name__ == '__main__':
    a,b,c = map(int,raw_input().split())
    is_triangle(a,b,c)
