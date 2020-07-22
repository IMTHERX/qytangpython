#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao
import re
from qytang_ping import qytang_ping # 负责检测ping
from qytang_ssh import qytang_ssh # 负责ssh到设备
from qytang_re import qytang_re # 负责处理接口信息
from pprint import pprint # 负责打印

def qytang_get_if(*ips,username="cisco",password="cisco"):
    device_if_dict = {} # 创建一个空的接口信息字典
    for ip in ips: # 循环判断每一个IP地址
        ping_result = qytang_ping(ip) # 记录ping结果，
        if ping_result == 1: # =1则通
            list_ssh_result = qytang_ssh(ip,username,password) # 进行筛选show ip route的接口&IP操作
            device_if_dict[ip] = qytang_re(list_ssh_result) # 将结果re处理后，直接存入字典中
        else:
            device_if_dict[ip] = {} # 由于无法ping通，存一下ping的目标IP，value为空
    return device_if_dict

if __name__ == '__main__':
    pprint(qytang_get_if('192.168.6.50','192.168.6.52','192.168.6.51'),indent = 4)