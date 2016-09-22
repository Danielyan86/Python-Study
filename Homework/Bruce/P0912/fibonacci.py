#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Fibonacci(object):

	def fibonacci(self, n):
		if n == 0 or n == 1:
			return n
		else:
			return self.fibonacci(n-1) + self.fibonacci(n-2)

	def run(self):
		while True:
			number = raw_input('Enter a number:')
			try:
				if len(number) < 1 :
					print "number can't be null"
				else :
					fibonacci_list = [self.fibonacci(x) for x in range(int(number))]
					print fibonacci_list
					exit()
			except Exception, e:
				print "Invalid input {0}".format(str(e))
				exit()
		
if __name__ == '__main__':
	f = Fibonacci()
	f.run()

