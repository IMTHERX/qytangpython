#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao
import datetime

# 获得5天前的时间
strtime_now = str(datetime.datetime.now()) # 获得现在的时间
strtime_fiveDayAgo = str(datetime.datetime.now() - datetime.timedelta(days = 5)) # 获得五天前的时间
print(strtime_now) # 测试
print(strtime_fiveDayAgo) # 测试

file_fiveDayAgo = open('save_fivedayage_time_' + str(strtime_now) + '.txt','w') # 创建文件
file_fiveDayAgo.write(str(strtime_fiveDayAgo)) # 写入str
file_fiveDayAgo.close() # 关闭会话

if __name__ == '__main__':
    pass