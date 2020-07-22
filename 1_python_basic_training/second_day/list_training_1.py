#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao

# 方法A
list1 = [6,8,3,4,1,2,5,9]
list2 = list1.copy() # 复制list1
list2.sort() # list2 单独排序
for i in range(len(list1)):
    print(list1[i],list2[i])

print( '=' * 30) # 分隔符

# 方法B
list1 = [50,99,8,77,66,5,44,33,22,11]
list2 = sorted(list1) # 引用排序后的list1
for i in range(len(list1)):
    print(list1[i],list2[i])