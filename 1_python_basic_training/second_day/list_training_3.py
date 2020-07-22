#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao
# 使用正则，找到ifconfig中的mac
import os
import re
ifconfig_result = os.popen('ifconfig ' + 'ens33').read() # 获取ifconfig信息
# print(ifconfig_result)  # 测试
# 正则匹配数据，前3行直接全部匹配，跳到MAC信息部分。
ifconfig_result_re = re.match('.*\s+'
                              '.*\s+'
                              '.*\s+'
                              '\S+\s+'
                              '([a-z0-9]{2}:[a-z0-9]{2}:[a-z0-9]{2}:'
                              '[a-z0-9]{2}:[a-z0-9]{2}:[a-z0-9]{2})',ifconfig_result).groups()
# 格式化输出
print(f'MAC Address : {ifconfig_result_re[0]}')
