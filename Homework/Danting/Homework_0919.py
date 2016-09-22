#!/usr/bin/env python

import os

def fileCount(path, type):
    fileList = os.listdir(path)
    count=0
    #print(fileList)
    for i in fileList:
        if os.path.splitext(i)[1] == '.yml':
            count+=1
    print("{0} {1} file in {2}" .format(count,type,path))

fileCount("/Users/danting.deng/qe-repository/gavel","xml")