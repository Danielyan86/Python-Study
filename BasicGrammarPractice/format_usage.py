'''
Created on 2013-12-11

@author: yannpxia
'''
name = (1, 2, 3)

# This is the old way to print the string
print "this is number serise:%s" % (name,)

# this is format function
print "this is number serise:%s" % format(name)

'''
format(value[, format_spec])
    Convert a value to a formatted representation, as controlled by format_spec. The interpretation of format_spec will depend on the type of the value argument, however there is a standard formatting syntax that is used by most built-in types: Format Specification Mini-Language.
    Note
    format(value, format_spec) merely calls value.__format__(format_spec).
'''

# format method is also could be used for replace the specil charactor in string
a = "this is number {0}. This is number {1}"
print a
print a.format('1', '2')
