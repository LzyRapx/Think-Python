#coding:utf-8

class Time(object):
    """"""

def print_time(time):
    print '%.2d:%.2d:%.2d' % (time.hours,time.minutes,time.seconds)

def is_after(t1,t2):
    return  t1 < t2

t1 = Time()
t1.hours = 10
t1.minutes = 7
t1.seconds = 5

t2 = Time()
t2.hours = 11
t2.minutes = 27
t2.seconds = 15

print_time(t1)
print_time(t2)