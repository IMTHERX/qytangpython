#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao

# 基础SSH 操作
import paramiko
import re
import os
# ssh = paramiko.SSHClient()
# ssh.load_system_host_keys()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect('192.168.98.222',port=22,username='root',password='wcnmxzh111',timeout=5,compress=True)
# stdin,stdout,stderr = ssh.exec_command('ls')
# x = stdout.read().decode()
# print(x)

# 更新为函数
def qytang_ssh(ip, username, password, port='22', cmd='ls'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # print(ip, username, password, port, cmd) # test
    ssh.connect(ip, port=port, username=username, password=password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x

# 调用qytang_ssh，登录获取linux的route
def ssh_get_route(ip, username, password):
    route_res = []
    route = qytang_ssh(ip,username,password,cmd='route -n')
    re_route = re.findall('\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}\s+' # 匹配Dst IP
                            '(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+' # 匹配GW IP
                            '\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}\s+' # 匹配mask
                            '(\w{1,2})\s+' # 匹配flags
                            '\d+\s+' # 匹配metric
                            '\d+\s+' # 匹配ref
                            '\d+\s+' # 匹配use
                            '[a-z]\S+\d',route) # 匹配int;list[2]~n-1为路由信息
    for i in range(len(re_route)):
        if 'UG' in re_route[i][1]: # 判断re后的list的1号位，flag是否为UG
          route_res = (re_route[i][0])
        else:
           pass
    return route_res



# qytang_ssh('192.168.98.222','root','wcnmxzh111')
if __name__ == '__main__':
    print(qytang_ssh('192.168.6.222','root','wcnmxzh111'))
    print(qytang_ssh('192.168.6.222','root','wcnmxzh111',cmd='pwd'))
    print('网关为：')
    print(ssh_get_route('192.168.6.222', 'root', 'wcnmxzh111'))