#!/usr/bin/env python
def reverseA(a):
    print "Solution 1 :Output :"+a[::-1]

def reverseB(a):
    b=list(a)
    b.reverse()
    print "Solution 2 :Output :"+"".join(b)

a="ABCDE"
print "Input :"+a
reverseA(a)
reverseB(a)
