#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao

import re

if_info = ['VlAN ID','MAC','Type','Interface'] # 设定信息栏
mac_1 = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'

mac_re = re.match(r'(\d+)\s+([0-9a-z]{4}\.[0-9a-z]{4}\.[0-9a-z]{4})\s+([A-Z]+)\s+([A-Z]\S+\d)',mac_1).groups()

print(f'{if_info[0]:<10}: {mac_re[0]}\n'
      f'{if_info[1]:<10}: {mac_re[1]}\n'
      f'{if_info[2]:<10}: {mac_re[2]}\n'
      f'{if_info[3]:<10}: {mac_re[3]}\n')