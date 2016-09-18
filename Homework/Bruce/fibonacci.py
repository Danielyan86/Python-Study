#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fibo(n):
	if n == 0 or n == 1:
		return n
	else:
		return fibo(n-1) + fibo(n-2)

def func(n):
	return [fibo(x) for x in range(n)]

def main():
	print func(8)

if __name__ == '__main__':
	main()

