#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao
# 参考https://www.jianshu.com/p/dfeb915d9188
compare_list = ['eth 1/101/1/7', 'eth 1/101/1/13', 'eth 1/101/1/18', 'eth 1/101/1/23',\
                'eth 1/101/1/25', 'eth 1/101/1/26', 'eth 1/101/1/32', 'eth 1/101/1/34',\
                'eth 1/101/1/42', 'eth 1/101/1/45', 'eth 1/101/2/8','eth 1/101/2/46']

port_list = ['eth 1/101/1/42','eth 1/101/1/26','eth 1/101/1/23','eth 1/101/1/7',\
             'eth 1/101/2/46','eth 1/101/1/34','eth 1/101/1/18','eth 1/101/1/13',\
             'eth 1/101/1/32','eth 1/101/1/25','eth 1/101/1/45','eth 1/101/2/8']
# sorted_port_list = sorted(port_list,key=lambda d : int(d.split(' ')[-1].split('/')[2]))

# 可以定制你想要的key, key= lambda x : (x[1], x[0]) 按二个元素，再第一个
sorted_port_list = sorted(port_list,key = lambda \
        d : (int(d.split(' ')[-1].split('/')[-2]),int(d.split(' ')[-1].split('/')[-1])))


for i in range(0,len(port_list)):
    print(port_list[i] + '   |   ' + sorted_port_list[i] + '   |   ' + compare_list[i])

# a = [(3,4),(2,5),(1,6)]
# b = sorted(a)
# c = sorted(a,key=lambda x: x[1])
#
# print(b)
# print(c)