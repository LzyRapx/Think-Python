#coding:utf-8

def countdown(n):
    if n<=0:
        print "Done!"
    else:
        print n
        countdown(n-1)

#countdown(5)

def do_n(f,n):
    if n<=0:
        return
    else:
        countdown(5)
        do_n(f,n-1)

do_n(countdown,5)
