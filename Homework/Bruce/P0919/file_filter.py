#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

class File(object):

	def run(self):
		path = raw_input('Input file path:')
		if len(path) < 1 :
			print "path can't be null"
			exit()
		elif not os.path.isdir(path):
			print "NOT found the path {0}".format(path)
			exit()


		file_type = raw_input('Input file type:')
		if len(file_type) < 1 :
			print "file type can't be null"
			exit()

		file_suffix = "." + file_type
		file_list = []

		for root,dirs,files in os.walk(path):
			for file in files:
				file_path = os.path.join(root, file)
				if os.path.isfile(file_path) and os.path.splitext(file_path)[1].lower() == file_suffix.lower():
					file_list.append(file_path)

		print "{0} {1} file{2} in path {3}".format(len(file_list), file_type, 's' if len(file_list)>1 else '', os.path.abspath(path))

if __name__ == '__main__':
	f = File()
	f.run()