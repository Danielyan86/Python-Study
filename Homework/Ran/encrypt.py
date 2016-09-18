s=raw_input("Please input a string:")
s1=list(s)
l=len(s)
for i in range(0,l):
	s1[i]=chr(ord(s[i])+3)
print s1