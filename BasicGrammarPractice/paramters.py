'''
Created on 2013-11-28

@author: yannpxia
'''


def parameter_usage(para1, *para2):
    print "para1 is:", para1
    for item in para2:
        print item


A = 0
list_A = [1, 2, 3]
# list A as a whole in the fisrt element in para2 list
parameter_usage(A, list_A)

# list A as seperate parameter in the fisrt element in para2 list
parameter_usage(A, *list_A)
