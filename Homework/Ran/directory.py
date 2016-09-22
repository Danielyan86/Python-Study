#!/usr/bin/env python
import os

count = 0


def filenumber(Dir, type):
    global count
    Dirs = os.listdir(Dir)
    for filename in Dirs:
        validname = os.path.join(Dir, filename)
        if os.path.isfile(validname) and os.path.splitext(filename)[1] == Type:
            print validname
            count += 1
        elif os.path.isdir(validname):
            filenumber(validname, Type)


Dir = raw_input("Please enter directory:")
Type = raw_input("Please enter the file type:")
Type = '.' + Type
filenumber(Dir, Type)
print "%d %s file in path %s" % (count, Type, Dir)