#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao

Department1 = 'Security'
Department2 = 'Python'
depart1_m = '王涛'
depart2_m = '李秀'
COURSE_FEES_Python = 6666.777
COURSE_FEES_SEC = 8888.222

# old function 1
line1 = ' Department: %-10s Depart: %-10s Fees: %-10s'%(Department1,depart1_m,COURSE_FEES_Python)
line2 = ' Department: %-10s Depart: %-10s Fees: %-10s'%(Department2,depart2_m,COURSE_FEES_SEC)
length = len(line1)
print("OLD function A")
print("=" * length)
print(line1)
print(line2)
print("=" * length)


# old function 2
line1 = ' Department: {0:10} Depart: {1:10} Fees: {2:<10.2f}'.format(Department1,depart1_m,COURSE_FEES_Python)
line2 = ' Department: {0:10} Depart: {1:10} Fees: {2:<10.3f}'.format(Department2,depart2_m,COURSE_FEES_SEC)
length = len(line1)
print("OLD function B")
print("=" * length)
print(line1)
print(line2)
print("=" * length)

# new function
line1 = f' Department: {Department1:10} Depart: {depart1_m:10} Fees: {COURSE_FEES_Python:<10.2f}'
line2 = f' Department: {Department2:10} Depart: {depart2_m:10} Fees: {COURSE_FEES_SEC:<10.3f}'
length = len(line1)
print("NEW function")
print("=" * length)
print(line1)
print(line2)
print("=" * length)
