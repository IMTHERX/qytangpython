#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao
# 题目要求，使用正则表达式，寻找到ifconfig中的ip地址
import os
import re
ifconfig_result = os.popen('ifconfig ' + 'ens33').read()
# print(ifconfig_result) #测试用

# 正则匹配IP地址等信息
ifconfig_result_re = re.match('(\w+\d+):\s+\S+\s+\w+\s+\d+\s+'
                              '\w+\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})'
                              '\s+\w+\s+'
                              '(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})'
                              '\s+\w+\s+'
                              '(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+'
                              '.*',ifconfig_result).groups()
# 输出IP 掩码 广播地址
print(f'Interface  ：{ifconfig_result_re[0]:<}\n'
      f'IP Address ：{ifconfig_result_re[1]:<}\n'
      f'netmask    : {ifconfig_result_re[2]:<}\n'
      f'broadcast  : {ifconfig_result_re[3]:<}\n')