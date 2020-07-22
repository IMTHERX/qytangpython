#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao
List1 = ['aaa',111,(4,5),2.01]
List2 = ['bbb',333,111,3.14,(4,5)]

# print(List1[0] in List2) # 测试是否能够比较返回值

for i in range(len(List1)):
    if List1[i] in List2:
        print(str(List1[i]) + ' is both in List1 & List2！')
    else:
        print(str(List1[i]) + ' is only in List1！')