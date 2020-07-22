#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao

# 写入文件
myfile = open('myfile.txt','w')
myfile.write('welcome to qytang\n')
myfile.write('this is python\n')
myfile.write('im wangtao\n')
myfile.close()

# 读取文件方法A
myfile = open('myfile.txt','r') # 一行一行读取
# print(myfile.readlines())

# 读取文件方法B，不推荐
myfile = open('myfile.txt').read() # 一下子全部读出，但是不推荐用read()；大文件有问题

# 读取文件方法C，文件迭代器方法：推荐使用此方法
for line in open('myfile.txt'):
    # print(line) # print本身会回车一次，所以加上txt中的 \n 合计2个回车
    print(line,end='') # 使不额外的换行

# 追加文本
myfile = open('myfile.txt','a')
myfile.write('hahahahahaha\n')
myfile.close()
# print(open('myfile.txt','r').readlines())
print(open('myfile.txt','rb').readlines()) # 通过字节字符串打开，解析ascii码，避免一些不兼容导致的报错

# 如果读取要从中间写，则可以用以下方法
myfile = open('myfile.txt','r+')

