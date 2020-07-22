#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao
import re
tcp_info = ['protocol','server','localserver','idle','bytes','flags']  # 设定信息栏
tcp_conn1 = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

# 正则match需要的内容
tcp_conn1_re = re.match('(\w+)\s+\w+\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d{1,5})'
                        '\s+\w+\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d{1,5})'
                        ',\s+\w+\s+(\d{1,2}:\d{1,2}:\d{1,2}),\s+\w+\s+'
                        '(\d+),\s+\w+\s+(\w+)',tcp_conn1).groups()
# 格式化输出
for i in range(0,len(tcp_conn1_re)):
    while i == 3: # 4号位固定为时间，所以i = 4-1 时，拆分00:12:23的时间
        idle_times = tcp_conn1_re[i].split(":") # 通过冒号拆分
        print(f'{tcp_info[i]:<13}: {idle_times[0]} 小时 {idle_times[1]} 分钟 {idle_times[2]} 秒 ') # 加入小时，分，秒
        break # 避免循环无法跳出
    else:
        print(f'{tcp_info[i]:<13}: {tcp_conn1_re[i]}')


# tcp_conn1_re = re.match('(\S+)\s+\S+\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}\S+)\s+\S+\s'
#                         '(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}\S+),\s+\S+\s+'
#                         '(\d{1,}:\d{1,}:\d{1,}),\s+\S+\s+(\d{1,}),\s+\S+\s+(\S+)',tcp_conn1).groups()
#
# print(f'{tcp_info[0]:<13}: {tcp_conn1_re[0]}')
# print(f'{tcp_info[1]:<13}: {tcp_conn1_re[1]}')
# print(f'{tcp_info[2]:<13}: {tcp_conn1_re[2]}')
# print(f'{tcp_info[3]:<13}: {tcp_conn1_re[3][0]}小时{tcp_conn1_re[3][2]}分钟{tcp_conn1_re[3][2]}秒')
# print(f'{tcp_info[4]:<13}: {tcp_conn1_re[4]}')
# print(f'{tcp_info[5]:<13}: {tcp_conn1_re[5]}')
