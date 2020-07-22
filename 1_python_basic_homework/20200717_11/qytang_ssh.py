#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao

# ssh函数
import paramiko
def qytang_ssh(ip, username='cisco', password='cisco', port='22', cmd='show ip interface brief'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=port, username=username, password=password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    result = stdout.read().decode()
    return result

if __name__ == '__main__':
    print(qytang_ssh('192.168.6.50','cisco','cisco')) # 测试登录路由器