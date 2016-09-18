#!/usr/bin/env python
# -*- coding: utf-8 -*-

def table(n):
	for i in range(1,n+1):
		for j in range(1,i+1):
			print str(j)+'x'+str(i)+'='+str(j*i),
		print ""

def main():
	n = raw_input('Enter a number for printing multiple table:')
	try:
		table(int(n))
	except Exception, e:
		print "Invalid input"


if __name__ == '__main__':
	main()