#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao

# 方法A
L1 = ['4','3','6','5','2','1'] # 创建L1
L2 = sorted(L1) # 降排序后的L1返回的数值，赋值给L2

# 方法B
L3 = ['10','19','20','15','18','11'] # 创建L3
L4 = L3.copy() # L4 赋值 L3的拷贝，否则会指向L3的内存，随着L3的变化而变化
L4.sort()

# 输出结果
print('引用      拷贝')
for i in range(len(L1)):
    print(L1[i],L2[i] + '   |  ' + L3[i],L4[i])
