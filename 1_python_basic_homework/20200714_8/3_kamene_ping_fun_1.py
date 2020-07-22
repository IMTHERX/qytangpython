#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao

# 创建一个简单的ping函数
import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *

# 将代码改为函数
def qytang_ping(ip):
    ping_pkt = IP(dst=str(ip))/ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return(str(ip) + ' 通！') # 返回值，可以用作输出
    else:
        return(str(ip) + ' 不通！') # 返回值，可以用作输出

if __name__ == '__main__':
    print(qytang_ping('192.168.98.1'))
