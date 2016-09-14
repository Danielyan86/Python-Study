#!/usr/bin/env python

print "Print 4*4 table"

def table(n,m):
    for i in range(n):
        line = ""
        for j in range(m):
            if i == 0: 
                line += str(j) + " "
            elif j == 0:
                line += str(i) + " "
            else:
                line += str(i*j) + " "
        print line

table(4,4)

