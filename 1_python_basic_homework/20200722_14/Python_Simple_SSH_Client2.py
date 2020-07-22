#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao
from argparse import ArgumentParser
import paramiko

def qyt_argparse(ipaddr, username, password,command): # 设定ssh
    # ssh = paramiko.SSHClient()
    # ssh.load_system_host_keys()
    # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ssh.connect(ipaddr, port=22, username=username, password=password, timeout=5, compress=True)
    # stdin, stdout, stderr = ssh.exec_command(command)
    # result = stdout.read().decode()
    # print(result)
    # return result
    print(ipaddr)
    print(username)
    print(password)
    print(command)

# 设定argument
usage = "Python Simple_SSH_Client -i ipaddr -u username -p password -c command" # 设定用法描述

parser = ArgumentParser(usage=usage)

parser.add_argument("-i", "--ipaddr", dest="ipaddr", help="SSH Server", default=0, type=str)
parser.add_argument("-u", "--username", dest="username", help="SSH Username", default=1, type=str)
parser.add_argument("-p", "--password", dest="password", help="SSH Password", default=2, type=str)
parser.add_argument("-c", "--command", dest="command", help="SSH Command", default=3, type=str)

args = parser.parse_args()

qyt_argparse(args.ipaddr, args.username, args.password, args.command)

if __name__ == '__main__':
    pass