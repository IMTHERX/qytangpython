#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao
import os
import re
route_result = os.popen('route -n').read() # 赋值route 信息
route_result_list = route_result.split('\n') # 通过split"\n"做一个新的列表，为for循环计算len做准备

# 计算len；从2~ n-1循环多次，可以复用
# 2: (跳过前两行文字，直接到路由部分做re匹配)
# n-1: (通过\n做split时，列表最后会有一个空列表，避免报错)
for i in range(2,len(route_result_list)-1):
    re_route_result_list = re.match('\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}\s+' # 匹配Dst IP
                                    '(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+' # 匹配GW IP
                                    '\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}\s+' # 匹配mask
                                    '(\w{1,2})\s+' # 匹配flags
                                    '\d+\s+' # 匹配metric
                                    '\d+\s+' # 匹配ref
                                    '\d+\s+' # 匹配use
                                    '[a-z]\S+\d',route_result_list[i]).groups() # 匹配int;list[2]~n-1为路由信息

    if 'UG' in re_route_result_list[1]: # 判断re后的list的1号位，flag是否为UG
        print('网关地址为：' + re_route_result_list[0])
    else:
        pass
