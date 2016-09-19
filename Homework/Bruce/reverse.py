#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Reverse(object):

	def run(self):
		while True:
			string = raw_input("enter string:")
			if len(string) < 1 :
				print "string can't be null"
			else:
				print string[::-1]
				exit()


if __name__ == '__main__':
	r = Reverse()
	r.run()

