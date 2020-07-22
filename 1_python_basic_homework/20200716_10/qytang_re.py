#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao
import re

def qytang_re(re_str):
    dict_re_str = {} # 创建空字典，用于将re.match的信息，存入字典中
    for i in range(len(re_str)):
        re_str_result = re.findall('\s*([fFgGlL]\S+\d)\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s*',re_str[i])
        # ↓ 将新的key&value写入字典
        if re_str_result: # 如果本次循环有获取到接口及IP信息，则处理，否则跳过
            dict_re_str[re_str_result[0][0]] = re_str_result[0][1]
        else:
            pass
    return dict_re_str

if __name__ == '__main__':
    # qytang_re(qytang_get_if('192.168.6.50'))
    pass