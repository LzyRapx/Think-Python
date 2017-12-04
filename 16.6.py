#coding:utf-8

from datetime import *
import dateutil

"""
1. 用 datetime 模块来写一个函数，获取当前日期，然后输出今天是星期几。
2.写一个函数，要求输入生日，然后输出用户的年龄以及距离下一个生日的日、时、分、秒
数。
3.有的两个人在不同日期出生，会在某一天，一个人的年龄是另外一个人年龄的两倍。这一天
就叫做他们的双倍日。写一个函数，接收两个生日，然后计算双倍日
"""

def print_daytoday():
    now = datetime.now()
    print now.strftime('%A')

#输出用户的年龄以及距离下一个生日的日、时、分、秒数。
def birthday_countdown(date):

    now = datetime.now()

    next_birthday = datetime(now.year, date.month, date.day)

    if next_birthday > now:
        delta = next_birthday - now
    else:
        next_birthday = datetime(now.year+1, date.month, date.day)
        delta = next_birthday - now
    print delta

birthday = datetime(1995, 1, 1)
birthday_countdown(birthday)

b1 = datetime(1995, 1, 1)
b2 = datetime(1996, 1, 1)

def double_day(b1, b2, times):
    elder = min(b1, b2)
    younger = max (b1, b2)
    days_elder = younger - elder
    days_elder = days_elder.days +1.0
    days_younger = 0 +1.0
    for day in range (999999):
        if int(days_elder/days_younger) == times:
            print days_elder, days_younger
            b1 = b1 + timedelta(days = days_elder)
            return
        days_elder += 1
        days_younger += 1
        count = day
    years = b1 + timedelta(days=count)

double_day(b1, b2, 10)
