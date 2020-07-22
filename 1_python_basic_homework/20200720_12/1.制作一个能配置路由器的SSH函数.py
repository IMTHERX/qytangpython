#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao
import paramiko
import time

'''
show ver,conf t,no router ospf 1,router ospf 1, network 192.168.6.0 0.0.0.255 area 0,end,sh ip ospf 1 statistics detail topology base
'''

def qytang_multicmd(ip, username, password, cmd_list=[], enable='', wait_time=2, verbose=True, port=22):
    cmd_list = input("请输入你的命令，并通过“逗号”隔开，例如：show run，show ip route。\n").split(',')
    enable_cmd_list = ['enable',enable] # 预设enable所需的命令行
    ssh = paramiko.SSHClient() # 创建SSH Client
    ssh.load_system_host_keys() # 加载系统SSH密钥
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # 添加新的SSH密钥
    ssh.connect(ip, port=port, username=username, password=password, timeout=5, compress=True)  # SSH连接
    print(f'正在连接主机{ip}...') # 让你知道脚本还在跑
    chan = ssh.invoke_shell() # 激活交互式shell
    if len(enable)>1: # 判断有无enable 权限
        for enable_cmd in enable_cmd_list: # 跑enable脚本
            time.sleep(0.5)  # 等待网络设备回应
            chan.send(str(enable_cmd) + '\n')  # 发送enable脚本的命令
            if verbose:
                print(f'正在执行\n{enable_cmd}...')
                # print('执行结果\n' + str(chan.recv(204800).decode()))

    if len(cmd_list)>1: # 判断有无cmd list
        chan.send('ter len 0 \n') # 预设ter len 0参数，全部输出
        for cmd in cmd_list: # 发送cmd命令
            time.sleep(int(wait_time))  # 等待网络设备回应
            chan.send(cmd + '\n')  # 发送命令
            print(f'正在执行\n{cmd}...') # 让人知道脚本在跑
            time.sleep(int(wait_time))  # 等待网络设备回应
            if verbose:
                print('执行结果\n' + str(chan.recv(204800).decode()))
        # buffer = chan.recv(204800).decode()  # 获取路由器返回的信息
        chan.close() # 关闭shell
        ssh.close() # 关闭ssh

    else: # 没有cmd命令，则直接结束
        buffer = chan.recv(204800).decode()  # 获取路由器返回的信息
        if verbose:
            print('执行结果\n' + str(buffer))
        chan.close()
        ssh.close()



if __name__ == '__main__':
    # qytang_multicmd('192.168.6.50','cisco','cisco') # 测试特权账户登录路由器
    qytang_multicmd('192.168.6.50', 'cisco1', 'cisco',enable='cisco')  # 测试低权限账户登录路由器