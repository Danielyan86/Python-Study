"""
Created on 2013-11-7

@author: xiaodong.yan
"""


# Assert statements are a convenient way to insert debugging assertions into a program:
def assert_usage():
    expression = False
    if __debug__:
        if not expression: raise AssertionError


def assert_usage2():
    expression = False
    if __debug__:
        print("enter")
        if expression: raise AssertionError("the satatement is false")


assert_usage()
assert_usage2()
