#coding:utf-8

from datetime import *
import dateutil

class Time(object):
    def time_to_int(self):
        minutes = self.hours * 60 + self.minutes
        seconds = minutes * 60 + self.seconds
        return seconds

t1 = Time()
t1.hours = 11
t1.minutes = 12
t1.seconds = 13

print t1.time_to_int()
