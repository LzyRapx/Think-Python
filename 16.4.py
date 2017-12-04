#coding:utf-8

class Time(object):
    """"""
def time_to_int(t):
    
    """
    Returns a time in seconds
    """
    minutes = t.hours * 60 + t.minutes
    seconds = minutes * 60 + t.seconds
    return seconds


def int_to_time(t):
    """
    Takes a time in seconds and returns it in format hh:mm:ss
    """
    time = Time()
    minutes, time.seconds = divmod(t, 60)
    time.hours, time.minutes = divmod(minutes, 60)
    return time

def print_time(time):
    print '%.2d:%.2d:%.2d' % (time.hours, time.minutes, time.seconds)

def increment(t, seconds):
    return int_to_time(time_to_int(t) + seconds)

t1 = Time()
t1.hours = 10
t1.minutes = 7
t1.seconds = 5

print_time(t1)
t2 = increment(t1, 4000)
print_time(t2)