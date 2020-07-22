#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao
from qytang_md5 import qytang_md5 # 负责计算md5
from qytang_ssh import qytang_ssh # 负责登录设备
import time

def qytang_get_config(ip,username='cisco',password='cisco'): # 调用ssh模块，获取配置
    try:  # 如果成功则返回config信息
        return qytang_ssh(ip, username, password, cmd='sh run | b hostname')
    except Exception: # 如果报错则返回空值
        return

def qytang_check_diff(ip,username='cisco',password='cisco'):
    before_qytang_md5 = qytang_md5(qytang_get_config(ip, username, password)) # 记录初始配置，计算产生初始md5
    while True:
        after_qytang_md5 = qytang_md5(qytang_get_config(ip, username, password)) # 更新配置，计算产生更新md5
        if before_qytang_md5 == after_qytang_md5: # 更新md5 == 初始md5 ，则配置未变更
            print(before_qytang_md5) # 输出md5
            time.sleep(5) # 等待5秒后再次对比md5
        else:
            print(str(after_qytang_md5) + '\nMD5 value changed')
            break

if __name__ == '__main__':
    qytang_check_diff('192.168.6.50')