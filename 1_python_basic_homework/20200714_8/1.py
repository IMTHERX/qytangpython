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
    # 输入netstat -tulnp，查看端口信息
    netstat_result = os.popen('netstat -tulnp').read()
    # print(netstat_result)

    # 直接用findall检测需要的端口信息，findall比较灵活，不像match，IPv6定义需要区别处理，否则报错
    # 抓取(TCP,端口号)用以判断
    re_netstat_result = re.findall('(\S+)\s*\d{1,3}\s*\d{1,3}\s*' # 获取TCP/UDP
                                   '\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:(\d{1,5})\s*' #获取端口信息
                                   '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\:\S+\s*'
                                   '\w+\s*\d+\/\S+', netstat_result)
    # print(re_netstat_result)
    check_prot = ('tcp','80') # 定义判断的基准(TCP,端口号)
    if check_prot in re_netstat_result: # 如果(TCP,端口号) = ('tcp','80') 则为真
        print('HTTP(TCP/80)服务已经被打开')
        break # 停止检测
    else:
        print('等待一秒重新开始监控！')
        time.sleep(1) # 等待1秒重新检测