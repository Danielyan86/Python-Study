# coding=utf-8
'''
Created on 2013-12-13

@author: xiaodong yan
'''
myTuple = (123, "xyz", 23, 1)
i = iter(myTuple)
print i.next()
print i.next()
print i.next()
print i.next()

print "this is a example of how iter() is used for dictionary"
myDic = {"a": 1, "b": 2, "c": 3, "d": 4}

i = iter(myDic)
print i.next()
print i.next()
print i.next()

'''This module implements a number of iterator building blocks inspired by constructs from APL, Haskell, and SML.
Each has been recast in a form suitable for Python.

The module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination.
Together, they form an “iterator algebra” making it possible to construct specialized tools succinctly and efficiently
 in pure Python.
https://docs.python.org/2/library/itertools.html?highlight=itertools#itertools.izip

'''
from itertools import izip, count, islice

for i in izip(count(10, 2), ['a', 'b', 'c']):
    print i


def lib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


print list(islice(lib(), 5*10))
