#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao

# 创建一个简单的ping函数
# 以下2句为了防止报错：
# WARNING: No route found for IPv6 destination :: (no default route?). This affects only IPv6
import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *

# 一个简单的ping包
# ping_pkt = IP(dst='192.168.98.1')/ICMP()
#
# ping_result = sr1(ping_pkt,timeout=2,verbose=False)
# ping_result.show()


# 将代码改为函数
def qytang_ping(ip):
    ping_pkt = IP(dst=str(ip))/ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        # ping_result.show()
        # print(str(ip) + ' 通！') # 第一次测试
        return(str(ip) + ' 通！') # 返回值，可以用作输出
        # return (1,ip) # 1表示ping成功，返回IP用于打印
    else:
        # print(str(ip) + ' 不通！') # 第一次测试
        return(str(ip) + ' 不通！') # 返回值，可以用作输出
        # return (0,ip) # 1表示ping失败，返回IP用于打印


if __name__ == '__main__':
    print(qytang_ping('192.168.98.1'))
    print(qytang_ping('192.168.98.2'))
    print(qytang_ping('223.5.5.5'))
    # result = qytang_ping('192.168.98.1')
    # if result[0] == 1:
    #     print(str(result[1]) + ' 通！')
    # else:
    #     print(str(result[1]) + ' 不通！')