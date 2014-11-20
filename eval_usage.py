'''
Created on 2013-12-10

@author: yannpxia

 eval(expression[, globals[, locals]])

 The arguments are a Unicode or Latin-1 encoded string and optional globals and locals. 
 If provided, globals must be a dictionary. If provided, locals can be any mapping object.
'''
x=1
print x+1

# eval will chang the variable of the expression to value
# in robotframe work this method is equal Evaluate
print eval('x+1') 