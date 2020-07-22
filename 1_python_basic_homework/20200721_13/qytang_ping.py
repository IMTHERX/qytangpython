#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao
# 将代码改为函数
import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *

class Qytang_ping: # 创建类
    def __init__(self,ip_input): # 定义初始参数
        self.dstip = ip_input
        self.srcip = None
        self.length = 100
        self.pkt = IP(dst=self.dstip, src=self.srcip) / ICMP()

    def srcip(self,srcip_input): # 设定srcip的方法
        self.srcip = srcip_input
        self.pkt = IP(dst=self.dstip, src=srcip) / ICMP()

    def size(self,length_input): # 设定修改size的方法
        self.length = length_input
        self.pkt = IP(dst=self.dstip, src=self.srcip) / ICMP()

    def one(self): # 设定ping1个包，且判断是否能通的方法
        result = sr1(self.pkt, timeout=1, verbose=False)
        if result: # 如果ping有结果，则为ping通
            return self.dstip + ' 通'
        else:
            return self.dstip + ' 不通'

    def ping(self): # 设置ping 5个包的方法
        res_ping = ''
        for i in range(5):
            result = sr1(self.pkt, timeout=1, verbose=False)
            if result:
                res_ping = res_ping + '!' # 返回str
                # print('!', end='', flush=True)
            else:
                res_ping = res_ping + '.' # 返回str
                # print('.', end='', flush=True)
        return res_ping  # 返回str

    def __str__(self): # 定义类的__str__，让人能看懂
        if not self.srcip:
            return (f'<{self.__class__.__name__} => dstip:{self.dstip}, size: {self.length}>')
        else:
            return (f'<{self.__class__.__name__} => srcip:{self.srcip}, dstip: {self.dstip}, size: {self.length}>')

class New_ping(Qytang_ping): # 新建一个ping，继承Qytang_ping
    def ping2(self): # 定义New_ping的方法与Qytang_ping类做区分测试
        res_ping = ''
        for i in range(5):
            result = sr1(self.pkt, timeout=1, verbose=False)
            if result:
                res_ping = res_ping + '+' # 与Qytang_ping类做区分测试
                # print('!', end='', flush=True)
            else:
                res_ping = res_ping + '?'
                # print('.', end='', flush=True)
        return res_ping

if __name__ == '__main__':
    ping_result = Qytang_ping('192.168.6.50')
    print(ping_result)