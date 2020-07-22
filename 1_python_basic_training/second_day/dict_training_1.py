#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao
# 把防火墙状态信息存储为字典，且格式化输出
import re
status1 = 'TCP Student 192.168.189.167:32111 Teacher 137.78.5.128:65111, idle 0:00:00, bytes 74, flags UIO'
status2 = 'TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65221, idle 0:00:03, bytes 334212, flags UIO'

# 匹配IP端口信息
re_status1 = re.match('\w+\s+\w+\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}):(\d{1,})\s+' # 获取sip,sip_port
                      '\w+\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}):(\d{1,}),\s+' # 获取dip,sip_port
                      '\w+\s+\d{1,2}:\d{1,2}:\d{1,2},\s+'
                      '\w+\s+(\w+),\s+\w+\s+(\w+)',status1).groups() # 获取type,flags

re_status2 = re.match('\w+\s+\w+\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}):(\d{1,})\s+' # 获取sip,sip_port
                      '\w+\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}):(\d{1,}),\s+' # 获取dip,sip_port
                      '\w+\s+\d{1,2}:\d{1,2}:\d{1,2},\s+'
                      '\w+\s+(\w+),\s+\w+\s+(\w+)',status2).groups() # 获取type,flags
# print(re_status1,re_status2) # 测试

# 组合字典
dict_status1 = {(re_status1[0],re_status1[1],re_status1[2],re_status1[3]):(re_status1[4],re_status1[5])}
dict_status2 = {(re_status2[0],re_status2[1],re_status2[2],re_status2[3]):(re_status2[4],re_status2[5])}
# 更新且打印字典
dict_status_all = {} # 创建一个空字典
dict_status_all.update(dict_status1) # 把字典status1更新到字典中
dict_status_all.update(dict_status2) # 把字典status2更新到字典中
print('打印字典：\n' + str(dict_status_all) + '\n')

# 格式化输出
printf_info = ['src','src_p','dst','dst_p','bytes','flags'] # 用于格式化输出
print('格式化打印输出：\n\n'
      f'{printf_info[0]:>10} : {re_status1[0]:<15} |' # 输出src ：src的IP地址
      f'{printf_info[1]:>10} : {re_status1[1]:<15} |' # 输出src_p ：src的prot号码
      f'{printf_info[2]:>10} : {re_status1[2]:<15} |' # 输出dst ：dst的IP地址
      f'{printf_info[3]:>10} : {re_status1[3]:<15} |\n' # 输出dst_p ：dst的prot号码
      f'{printf_info[4]:>10} : {re_status1[4]:<15} |' # 输出bytes ：bytes的数值
      f'{printf_info[5]:>10} : {re_status1[5]:<15} |') # 输出flags ：flags的数值
print('=' * 120)
print(f'{printf_info[0]:>10} : {re_status2[0]:<15} |'
      f'{printf_info[1]:>10} : {re_status2[1]:<15} |'
      f'{printf_info[2]:>10} : {re_status2[2]:<15} |'
      f'{printf_info[3]:>10} : {re_status2[3]:<15} |\n'
      f'{printf_info[4]:>10} : {re_status2[4]:<15} |'
      f'{printf_info[5]:>10} : {re_status2[5]:<15} |')
print('=' * 120)