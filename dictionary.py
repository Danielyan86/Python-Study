'''
Created on 2013-11-18

@author: yannpxia
'''
dic_example={"1":"A","2":[]}

print dic_example

print len(dic_example)
print "--------------------values------------------------------"
print dic_example.values()
if "" in dic_example.values():
    print "llllll"

#judge weather there is  a value in dictionary
if "" in dic_example:
    print True