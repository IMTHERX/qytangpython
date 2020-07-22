#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao

class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job
    def getlastname(self):
        return self.name.split()[-1]

    def giveraise(self,percent):
        self.pay *= (1.0 + percent)

if __name__ == '__main__':
    bob = Person('Bob Sb',42,10000,'se')
    # print(bob.name.split()[-1])
    print(bob.getlastname())

    # print(bob.age * 2)

    print(int(bob.pay))
    bob.giveraise(0.5)
    print(bob.pay)

    # print(bob.job)

