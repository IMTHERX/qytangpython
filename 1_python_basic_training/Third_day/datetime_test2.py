#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao
from datetime import timedelta, timezone, datetime
from dateutil import parser


# 切时区
tz_8 = timezone(timedelta(hours=8))
print(datetime.now().astimezone(tz_8))
tz_1 = timezone(timedelta(hours=1))
print(datetime.now().astimezone(tz_1))
print(tz_8)

if __name__ == '__main__':
    pass