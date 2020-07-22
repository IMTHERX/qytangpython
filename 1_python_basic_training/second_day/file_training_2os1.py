#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao

import os

# os.getcwd()获取当前目录，os.listdir罗列特定目录
# filelist = os.listdir(os.getcwd())
# print(filelist)

# os.rename 重命名文件
# os.rename('myfile.txt','testrename.txt')
# filelist = os.listdir(os.getcwd())
# print(filelist)
#
# os.rename('testrename.txt','myfile.txt')
# filelist = os.listdir(os.getcwd())
# print(filelist)

# os.remove 文件 : 最好别练这个！！！！
# myfile = open('myfile_remove.txt','w')
# myfile.close()
# filelist = os.listdir(os.getcwd())
# print(filelist)
# os.remove('myfile_remove.txt')
# filelist = os.listdir(os.getcwd())
# print(filelist)

# 判断是否为目录
filelist = os.listdir(os.getcwd())
print(filelist)
print(os.path.isdir('venv'))
print(os.path.isdir('README.md'))
print(os.path.isfile('../../README.md'))