#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao
# 将代码改为函数
import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *

def qytang_ping(ip):
    ping_pkt = IP(dst=str(ip))/ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        # print(str(ip) + ' 通！') # 测试
        return 1
    else:
        # print(str(ip) + ' 不通！')  # 测试
        return 0

if __name__ == '__main__':
    print(qytang_ping('192.168.6.51'))