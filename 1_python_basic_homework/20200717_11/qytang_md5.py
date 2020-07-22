#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao
# 如何计算字符串的MD5值
import hashlib

def qytang_md5(get_config):
    md5 = hashlib.md5()
    md5.update(get_config.encode())
    return md5.hexdigest()

if __name__ == '__main__':
    print(qytang_md5('tes1'))