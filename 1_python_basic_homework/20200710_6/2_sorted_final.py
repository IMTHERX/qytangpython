#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao
# 参考https://www.jianshu.com/p/dfeb915d9188
# 对比用的列表
compare_list = ['eth 1/101/1/7', 'eth 1/101/1/13', 'eth 1/101/1/18', 'eth 1/101/1/23',
                'eth 1/101/1/25', 'eth 1/101/1/26', 'eth 1/101/1/32', 'eth 1/101/1/34',
                'eth 1/101/1/42', 'eth 1/101/1/45', 'eth 1/101/2/8','eth 1/101/2/46']
# 题目中原始的列表
port_list = ['eth 1/101/1/42','eth 1/101/1/26','eth 1/101/1/23','eth 1/101/1/7',
             'eth 1/101/2/46','eth 1/101/1/34','eth 1/101/1/18','eth 1/101/1/13',
             'eth 1/101/1/32','eth 1/101/1/25','eth 1/101/1/45','eth 1/101/2/8']

# 可以定制你想要的key, key= lambda x : (x[1], x[0]) 按二个元素，再第一个
sorted_port_list = sorted(port_list,key = lambda x:
                    (int(x.split(' ')[-1].split('/')[-2]),
                     int(x.split(' ')[-1].split('/')[-1])))
# 格式化打印对比排序前后的list
print('原始list' + '          ' +'排序后list' +  '         ' + '对比参考list')
for i in range(0,len(port_list)):
    print(f'{port_list[i]:<15} | {sorted_port_list[i]:<15} | {sorted_port_list[i]:<15}')