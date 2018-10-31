# -*- coding: utf-8 -*-
"""
Created on 2013-11-28

@author: yannpxia
"""


def parameter_usage(para1, *para2):
    print "-------Enter the function to print parameter-------"
    print "para1 is:{0}".format(para1)
    print "para2 is:{0}".format(para2)
    for item in para2:
        print item


A = 1
list_A = [2, 3, 4]
# list A as a whole in the fisrt element in para2 list
parameter_usage(A, list_A)

# list A as seperate parameter in the fisrt element in para2 list
parameter_usage(A, *list_A)

# 这里记住的是类型是属于对象的，而不是变量。而对象有两种,“可更改”（mutable）与“不可更改”（immutable）对象。在python中，strings, tuples,
# 和numbers是不可更改的对象，而list,dict等则是可以修改的对象。(这就是这个问题的重点)

a = 1


def fun(a):
    a = 2


print a  # 1

a = []


def fun(a):
    a.append(1)


print a  # [1]
