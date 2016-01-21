"""
Created on 2013-12-9

@author: yannpxia
"""

import re

print "This is Example 1:"
""" 1. there is no groups() class is returned when there are no brackets in regular expression
    2. Number of brackets is matched with length of outpu tuple
"""
pattern = "MON|TUE"
data = "TUE MON asdf asdfkj falskdjmonMONfljoweut MON TUE vcxvuxoi TUE 423io4u"

reg2 = re.match(pattern, data)
print reg2.group()
# The return value is empty
print reg2.groups()

print "\n This is Example 2:"
pattern = "(MON) (TUE)"
reg1 = re.search(pattern, data)
m = reg1.groups()
print reg1.group()
print reg1.groups(1)
print reg1.groups()
m = reg1.groups()
for item in m:
    print item

print "Example 3:"
pattern = "as(\w+)"
reg1 = re.search(pattern, data)
m = reg1.groups()
print "-------------------------------"
print reg1.group()
print reg1.groups(1)
print "'reg1.groups() is'"
print reg1.groups()

print "re.compile testing"
reg = re.compile(pattern)
m = reg.search(data)
print m.groups()
