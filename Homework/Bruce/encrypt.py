#!/usr/bin/env python
# -*- coding: utf-8 -*-

def encrypt(s):
	return "".join(map(lambda x:chr(ord(x)+3), list(s)))


def main():
	s = 'ABC'
	print encrypt(s)

if __name__ == '__main__':
	main()

