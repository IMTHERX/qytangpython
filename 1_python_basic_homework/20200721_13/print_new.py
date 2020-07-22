#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao
from qytang_ping import Qytang_ping
from qytang_ping import New_ping


def print_new(word, s='-'):
    # print('{0}{1}{2}'.format(s * int((70 - len(word))/2), word, s * int((70 - len(word))/2)))
    set_off = s * int((70 - len(word))/2)
    print(f'{set_off}{word}{set_off}')

if __name__ == '__main__':
    ping_result = Qytang_ping('192.168.6.50')

    print_new('print class')
    print(ping_result) # 打印类

    print_new('ping one for sure reachable')
    print(ping_result.one()) # 打印ping的结果

    print_new('ping five')
    print(ping_result.ping()) # 打印ping 5次的结果

    print_new('set payload')
    ping_result.length = 200 # 修改payload
    print(ping_result) # 打印类
    print(ping_result.ping()) # 打印ping 5次的结果

    print_new('set ping src ip add')
    ping_result.srcip = '192.168.6.123' # 修改src ip 地址
    print(ping_result) # 查看类，确认src ip修改生效
    print(ping_result.ping())

    print_new('new class new ping','=')
    new_ping = New_ping('192.168.6.50')
    new_ping.length = 200
    print(new_ping)
    print(new_ping.ping2())

