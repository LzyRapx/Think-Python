#coding:utf-8

def ack(m, n):
    """
    Evaluates the Ackermann function
    m, n: positive integer numbers
    """
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))
    else:
        print 'Error, you probably entered a negative or non-integer number.'

print ack(3, 4)
