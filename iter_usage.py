'''
Created on 2013-12-13

@author: yannpxia
'''
myTuple=(123,"xyz",23,1)
i = iter(myTuple)
print i.next()
print i.next()
print i.next()
print i.next()


print "this is a example of how iter() is used for dictionary"
myDic = {"a":1,"b":2,"c":3,"d":4}

i = iter(myDic)
print i.next()
print i.next()
print i.next()