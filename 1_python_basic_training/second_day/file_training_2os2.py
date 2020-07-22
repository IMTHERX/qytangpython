#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao
# 查找包含qytang的文件（我的目录下没有qytang，则使用list代替）
import re
import os
# os.getcwd()获取当前目录，os.listdir罗列特定目录
filelist = os.listdir(os.getcwd())
print(str(filelist) + '\n文件夹中，包含list的文件为：')
# 判断如果找到list[i]中包含关键词，则打印这个i位元素否则跳过。
for i in range(len(filelist)):
    if re.findall('list',filelist[i]): # 当filelist[i]元组中包含list,则为真
        print(filelist[i])
    else:
        pass