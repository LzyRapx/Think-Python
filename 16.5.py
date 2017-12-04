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

def mul_time(t,number):
    return int_to_time(time_to_int(t) * number)


t1 = Time()
t1.hours = 10
t1.minutes = 7
t1.seconds = 5

print_time(t1)
t2 = increment(t1, 20)
print_time(t2)

def time_per_km(finish_time,km):
    # finish time in seconds
    ft_in_sc = time_to_int(finish_time)
    # How many seconds per km?
    sc_per_km = ft_in_sc / km
    # how much are these seconds as a time object
    return int_to_time(sc_per_km)

x = time_per_km(t1, 500)
print '\n'
print_time(x)
