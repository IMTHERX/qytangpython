#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao
import re
asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n " \
           "TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"
list_asa_conn = asa_conn.split('\n') # 通过\n拆分为列表，用以for循环复用处理

dict_asa_conn = {} # 创建空字典，用于将re.match的信息，存入字典中
for i in range(0,len(list_asa_conn)): # 循环matchIP信息
    re_asa_conn = re.match('\s*\w+\s+\w+\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}):(\d{1,})\s+'  # 获取sip,sip_port
                          '\s*\w+\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}):(\d{1,}),\s+'  # 获取dip,sip_port
                          '\s*\w+\s+\d{1,2}:\d{1,2}:\d{1,2},\s+'
                          '\s*\w+\s+(\w+),\s+\w+\s+(\w+)', list_asa_conn[i]).groups()  # 获取type,flags
    # ↓ 将新的key&value写入字典
    dict_asa_conn[re_asa_conn[0], re_asa_conn[1], re_asa_conn[2], re_asa_conn[3]] = \
        re_asa_conn[4], re_asa_conn[5]
print('打印字典\n' + str(dict_asa_conn) + '\n\n')
# 格式化输出
printf_info = ['src','src_p','dst','dst_p','bytes','flags'] # 用于格式化输出
print('格式化打印输出：')
for key,value in dict_asa_conn.items():
    print(f'{printf_info[0]:>10} : {key[0]:<15} | ' # 输出src ：src的IP地址
          f'{printf_info[1]:>10} : {key[1]:<15} | ' # 输出src_p ：src的prot号码
          f'{printf_info[2]:>10} : {key[2]:<15} |' # 输出dst ：dst的IP地址
          f'{printf_info[3]:>10} : {key[3]:<15} | \n' # 输出dst_p ：dst的prot号码
          f'{printf_info[4]:>10} : {value[0]:<15} | ' # 输出bytes ：bytes的数值
          f'{printf_info[5]:>10} : {value[1]:<15} | ') # 输出flags ：flags的数值
    print('=' * 122)