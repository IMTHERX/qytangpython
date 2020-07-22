#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao
import datetime
from dateutil import parser

# 简单测试
# now = datetime.datetime.now()
# print(now)
# print(datetime.datetime)
#
# print(now.strftime('%Y-%m-%d %H:%M:%S')) # 获得格式化的时间
# print(type(now.strftime('%Y-%m-%d %H:%M:%S')))
#
# print(now.strftime('%H:%M:%S'))
#
# print(now.year)
# print(now.day)

# 获得 几天前的时间
# threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days = 3)) # 3天前的现在
# print(threeDayAgo)

# # 获得 几天前的日期
# today = datetime.date.today()
# fiveDayAgo = (today - datetime.timedelta(days = 5)) # 5天前的现在
# print(fiveDayAgo)

# str 转 datetime的模块   pip3 install python-dateutil
strtime = str(datetime.datetime.now())
# datetime_obj = parser.parse(strtime)
print(type(strtime))
print(strtime)

if __name__ == '__main__':
    pass