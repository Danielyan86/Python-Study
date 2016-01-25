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
