#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

class How_Many_Files(object):

    def how_many_files(self, path, fileType):
        # cwd = os.getcwd()  # get current dir
        file_path = os.path.abspath(path) # into path, based on current dir
        list_all_files = os.listdir(file_path)  # list all files into list list_all_files
        file_number = 0
        for one_file in list_all_files:
            if self.is_type_match_2(one_file,fileType):
                file_number += 1
        return file_number

    def is_type_match_1(self, fileName, fileType):
        # find method return index of matched substring(fileType)
        if fileName.find('.'+fileType) > 0:
            return True
        else: return False

    # is_type_match_2 is better than is_type_math_1
    def is_type_match_2(self, fileName, fileType):
        # str split method split a string to a list(array) by '.'
        array = fileName.split('.')
        if  fileType == array[-1]:
            return True
        else: return False

    def run(self):
        path = 'testdir';
        print self.how_many_files(path,'xml')
        print self.how_many_files(path,'txt')
        print self.how_many_files(path,'word')

if __name__ == '__main__':
	e = How_Many_Files()
	e.run()