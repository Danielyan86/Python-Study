'''
Created on 2013-11-28

@author: yannpxia
'''


def parameter_usage(para1, *para2):
    print "para1 is:", para1
    for item in para2:
        print item



A=0
list_A=[1, 2, 3]
#list A as a whole in the fisrt element in para2 list
parameter_usage(A, list_A)

#list A as seperate parameter in the fisrt element in para2 list
parameter_usage(A, *list_A)

# 不定参数传参方式：如果没有默认值，name，month必须要有值，year，day可有可无
def test_para(name, month, year='', day=''):
    print name, month, year, day


para_tset = { 'month':"12",'day':"22",'name':"xiaodong" }
test_para(**para_tset)