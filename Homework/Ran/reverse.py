#!/usr/bin/env python
def method1(s):
	s=s[::-1]
	print s

def method2(s):
	s1=list(s)
	length=len(s)
	j=length-1
	for i in range(0,j+1):
		s1[i],s1[j]=s[j],s[i]
		j=j-1
	print s1

s=raw_input("please enter the string:")
method1(s)
method2(s)