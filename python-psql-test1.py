#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao

import pg8000
conn = pg8000.connect(host='192.168.98.223', user='qytangdbuser', password='',database='qytangdb')
#连接数据库
cursor = conn.cursor()#执行数据库操作
cursor.execute('create table test1(t1 int, t2 varchar(40))')#创建表
cursor.execute("insert into test1 (t1,t2) values (11, 'welcome to gytang')")#插入条目
cursor.execute("insert into test1 (t1,t2) values (12, 'welcome to Python')")
cursor.execute('select * from test1')
yourresults = cursor.fetchall()

print(yourresults) #直接可以看到是元组

for i in range(len(yourresults)): #另一种show的形式
    print(yourresults[i])

cursor.execute("drop table test1") #删除数据库
conn.commit() #严重注意一定要提交,否则数据不会实际写入数据库表
