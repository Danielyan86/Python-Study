#!/usr/bin/env python

def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

print "Print Fibonacci for 20"
for i in range(20):
    print F(i)
