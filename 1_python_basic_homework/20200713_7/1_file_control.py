#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao
import os
# 基础配置，创建测试用的文件
# os.mkdir('test') # 创建test目录
os.chdir('test') # 选择test目录为浏览路径
# qytang1 = open('qytang1','w')
# qytang1.write('test file\n')
# qytang1.write('this is qytang\n')
# qytang1.close()
# qytang2 = open('qytang2','w')
# qytang2.write('test file\n')
# qytang2.write('qytang python\n')
# qytang2.close()
# qytang3 = open('qytang3','w')
# qytang3.write('test file\n')
# qytang3.write('this is python\n')
# qytang3.close()
# os.mkdir('qytang4')
# os.mkdir('qytang5')

# os.getcwd()获取当前目录，os.listdir罗列特定目录
filelist = os.listdir(os.getcwd())
# print(filelist)

# 方法A,判断是否为文件，否则跳过不尝试打开。
# for file_or_dir in filelist:
#     if os.path.isfile(file_or_dir): # 判断是否为文件
#         if 'qytang' in open(file_or_dir,'r').read():
#             print('qytang in ' + file_or_dir)
#         else:
#             print('no qytang in ' + file_or_dir)
#     else:
#         pass

# 方法B 参考https://www.runoob.com/python/os-walk.html
for root,dirs,files in os.walk(os.getcwd(),topdown=True):
    for file in files:
        if 'qytang' in open(file,'r').read():
            print('qytang in ' + file)
        else:
            print('qytang not in ' + file)

# 清理test目录
os.chdir('..')
# print(os.listdir(os.getcwd()))

for root,dirs,files in os.walk('test',topdown=False):
    # print(root,dirs,files)
    for name in files: # 查找全部文件，并输出路径
        # print('files: ' + str(os.path.join(root,name)))
        os.remove(os.path.join(root,name)) # 清理文件
    for name in dirs: # 查找全部文件，并输出路径
        # print('dirs: ' + str(os.path.join(root, name)))
        os.rmdir(os.path.join(root, name)) # 清理目录

os.chdir('test')
print(os.listdir(os.getcwd()))