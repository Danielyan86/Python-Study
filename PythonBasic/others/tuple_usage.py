"""
Created on 2013-11-13

@author: yannpxia
"""
old_tuple = ("ABCD", "2", "3")
new_tuple = ()

print type(tuple(old_tuple[0]))
new_tuple = new_tuple + tuple(old_tuple[0])

print new_tuple

import operator

x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.iteritems(), key=operator.itemgetter(1))
print sorted_x

a = ("abc", "x")
b = ("def")
c = a + b
print c
print type(c)
print tuple(a + b)

a = ["abc"]
b = ["def"]
print a + b
a = "abc"
print tuple(a)
