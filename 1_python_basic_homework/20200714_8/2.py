#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao
# 定义l1，l2中的元素
list1 = ['aaa', 111, (4, 5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4, 5)]
# 方案1，非函数的形式
# for i in range(len(list1)):
#     if list1[i] in list2: # 一个一个的判断，list[i]的元素是否在list2内。
#         print(str(list1[i]) + ' is both in List1 & List2！') # 如果真则同时在List1，List2内。
#     else:
#         print(str(list1[i]) + ' is only in List1！') # 否则只是在List1内。

# 方案2，函数
def qytang_for(list1,list2):
    res = []
    for i in range(len(list1)):
        if list1[i] in list2:  # 一个一个的判断，list[i]的元素是否在list2内。
            res.append(str(list1[i]) + ' is both in List1 & List2！') # 把输出结果添加到res内
        else:
            res.append(str(list1[i]) + ' is only in List1！')
    return res # 返回res到函数

if __name__ == '__main__':
    result = qytang_for(list1,list2)
    for i in result:
        print(i)