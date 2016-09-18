i=int(input("the range of Fibonacci:"))
Feb=[]
if i==0:
	Feb.append(0)
elif i==1:
	Feb.append(1)
else:
	Feb=[0,1]
	for x in range (2,i-1):
		temp=Feb[x-1]+Feb[x-2]
		Feb.append(temp)
print Feb