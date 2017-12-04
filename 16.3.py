#coding:utf-8

class Time(object):
    """"""

def print_time(time):
    print '%.2d:%.2d:%.2d' % (time.hours,time.minutes,time.seconds)

def wrapper(entity):
    number_in_bigger = entity / 60
    remainder = entity % 60
    return number_in_bigger, remainder


def increment(time, seconds):

    if time.seconds + seconds < 60:
        time.seconds += seconds
        return

    min_in_sec, rem_sec = wrapper(seconds)

    if time.minutes + min_in_sec < 60:
        time.minutes += min_in_sec
        time.seconds += rem_sec
        return

    hour_in_min, rem_min = wrapper(min_in_sec)

    if time.hours + hour_in_min < 24:
        time.hours += hour_in_min
        time.minutes += rem_min
        time.seconds += rem_sec
        return

t1 = Time()
t1.hours = 10
t1.minutes = 7
t1.seconds = 5

print_time(t1)
increment(t1, 4000)
print_time(t1)