#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

class How_Many_Files(object):
    # in this method, path is defined;
    # need update later, make path as a parameter
    def how_many_files(self, fileType):
        # cwd = os.getcwd()  # get current dir
        test1 = os.path.abspath('testdir') # into 'testdir'
        list_all_files = os.listdir(test1)  # list all files into list list_all_files
        file_number = 0
        for one_file in list_all_files:
            if one_file.find(fileType) > 0:   # find method return index of matched substring(fileType)
                file_number = file_number + 1
        return file_number


    def run(self):
        print self.how_many_files('xml')
        print self.how_many_files('txt')
        print self.how_many_files('word')

if __name__ == '__main__':
	e = How_Many_Files()
	e.run()