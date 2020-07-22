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

# os.getcwd()获取当前目录
filelist = os.listdir(os.getcwd())

# 方法A,判断是否为文件，否则跳过不尝试打开。
# print('方法A：一般的for循环')
# for file_or_dir in filelist:
#     if os.path.isfile(file_or_dir): # 判断是否为文件
#         if 'qytang' in open(file_or_dir,'r').read():
#             print('qytang in ' + file_or_dir)
#             print('读取的文件内容为：\n' + str(open(file_or_dir,'r').read()))
#         else:
#             print('qytang not in ' + str(file_or_dir))

# 方法B 参考https://www.runoob.com/python/os-walk.html
print('\n方法B：更加方便的os.walk')
for root,dirs,files in os.walk(os.getcwd(),topdown=True):
    for file in files:
        if 'qytang' in open(file,'r').read():
            # print('qytang in ' + file)
            print('读取的文件内容为：\n' + str(open(file,'r').read()))
        else:
            print('qytang not in ' + file)
            print('读取的文件内容为：\n' + str(open(file, 'r').read()))

# 清理test目录
# os.chdir('..')
# print('\n清理文件操作：')
# for root,dirs,files in os.walk('test',topdown=False):
#     for name in files: # 查找全部文件，并输出路径
#         print('删除文件： ' + str(os.path.join(root,name)))
#         os.remove(os.path.join(root,name)) # 清理文件
#     for name in dirs: # 查找全部文件，并输出路径
#         print('删除目录： ' + str(os.path.join(root, name)))
#         os.rmdir(os.path.join(root, name)) # 清理目录
# os.removedirs('test')
# print('最终确认目录包含' + str(len(os.listdir(os.getcwd()))) + '个文件,详情如下：\n'
#                                                       + str(os.listdir(os.getcwd()))) # 确认test目录下文件被清除