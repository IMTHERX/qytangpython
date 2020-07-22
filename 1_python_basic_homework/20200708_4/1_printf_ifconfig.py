#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao
import random
import os
import re
# 获取网络接口信息
ifconfig_result = os.popen('ifconfig ' + 'ens33').read() # 获取接口配置信息
# print(ifconfig_result) # 测试打印接口配置信息


# 正则匹配IP地址，掩码，广播，mac地址
IPv4_address = re.findall('(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})',ifconfig_result)[0]
netmask = re.findall('(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})',ifconfig_result)[1]
broadcast = re.findall('(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})',ifconfig_result)[2]
MAC_Address = re.findall('(\S{2}:\S{2}:\S{2}:\S{2}:\S{2}:\S{2})',ifconfig_result)[0]



# 格式化输出IP 掩码 广播地址以及mac
print(f'IPv4 Address   ：{IPv4_address:<}\n'
      f'netmask        ：{netmask:<}\n'
      f'broadcast      : {broadcast:<}\n'
      f'MAC Address    : {MAC_Address:<}\n')

# 产生网关
IPv4_gw_host = str(random.randint(1,2)) # 随机假设网关的主机位
IPv4_gw = re.findall('(\d{1,3}.\d{1,3}.\d{1,3}.)',IPv4_address)[0] + str(random.randint(1,2)) # 随机产生一个网关地址
# IPv4_gw = re.findall('(\d{1,3}.\d{1,3}.\d{1,3}.)',IPv4_address)[0] + IPv4_gw_host # 随机产生一个网关地址
print('我假设网关的主机位为：' + IPv4_gw_host + '，因此网关地址为：' + IPv4_gw)

# ping 网关
ping_result = os.popen('ping ' + IPv4_gw + ' -c 1').read() # 获取接口配置信息
# print(ping_result)

# 验证网关连通性
re_ping_result = re.findall('[+]\w+\s+([er]\w+)',ping_result)
# print(re_ping_result)

if re_ping_result:
    print('ping网关：' + IPv4_gw + '失败！')
else:
    print('ping网关：' + IPv4_gw + '成功！')