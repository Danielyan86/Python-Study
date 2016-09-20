#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Encrypt(object):

	def encrypt(self,text):
		str1 = '';
		for t in text:
			t = chr(ord(t) + 3)
			str1 = str1 + t
		return str1


	def run(self):
		while True:
			string = raw_input('Enter a string for encrypting:')
			if len(string) < 1 :
				print "string can't be null"
			else:
				print self.encrypt(string)
				exit()

if __name__ == '__main__':
	e = Encrypt()
	e.run()

