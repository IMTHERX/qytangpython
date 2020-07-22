#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao
# 思路:
#     1:检测端口服务状态
#     2：如果有tcp80端口，则关闭检测
#     3：否则，休息1秒，再次检测

import os
import re
import time

while True:
    # 输入netstat -tulnp，查看端口信息，并拆一个list循环检测使用
    netstat_result = os.popen('netstat -tulnp').read()
    # print(netstat_result)

    # 直接用findall检测需要的端口信息，findall比较灵活，不像match，IPv6定义需要区别处理，否则报错
    re_netstat_result = re.findall('(\S+)\s*\d{1,3}\s*\d{1,3}\s*' # 获取TCP/UDP
                                   '\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:(\d{1,5})\s*' #获取端口信息
                                   '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\:\S+\s*'
                                   '\w+\s*\d+\/\S+', netstat_result)
    # print(re_netstat_result)
    check_prot = ('tcp','80') # 定义检测的基准;re_netstat_result获取的list内为元组(x,y)
    if check_prot in re_netstat_result: # 判断是否满足基准
        print('已检测到HTTP(tcp/80)服务，停止检测。')
        break
    else:
        print('未检测到HTTP(tcp/80)服务，1S后重新检测。')
        time.sleep(0.1)


