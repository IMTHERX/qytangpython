#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao

import re
ip_interface1 = 'Port-channel11.1        192.168.1.1   YES   CONFIG   up'
mac_address1 = '1024 0020.ed14.399c DYNAMIC Gi0/1'

# 格式化打印IP信息 interface1
ip_interface_result = re.match('([a-zA-Z]\S+\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+YES+\s+CONFIG\s+([a-z]+)'\
                               ,ip_interface1).groups()
print('接口IP信息\n' +
      f'接口   : {ip_interface_result[0]}\nIP地址 : {ip_interface_result[1]}\n状态   : {ip_interface_result[2]}')

# 格式化打印MAC信息
null = ['']
print('\n\n\n接口MAC信息\n'
              f'Vlan:{null[0]:20}MAC Address:{null[0]:14}Interface:{null[0]:15}')
# mac_address1
mac_address_result = re.match('(\S+)\s+([a-z0-9]{4}\.[a-z0-9]{4}\.[a-z0-9]{4})\s+[A-Z]+\s+([A-Z]\S+)'\
                               ,mac_address1).groups()
print(f'{mac_address_result[0]:25}{mac_address_result[1]:26}{mac_address_result[2]:15}')
