#!/usr/bin/env python

def reverse1(string):
    return string[::-1]

def reverse2(string):
    new_string=""
    length=len(string)-1
    while (length >= 0):
        new_string += string[length]
        length-=1
    return new_string

def encrypt(string):
    new_string=""
    length=len(string)
    for i in range(0,length):
        new_string+=chr(ord(string[i])+3)
    return new_string

def Fibon(n):
    if n==1:
        F_n=1
    elif n==0:
        F_n=0
    else:
        F_n=Fibon(n-1)+Fibon(n-2)
    return F_n

def Multiple_table():
    for i in range(1, 10) :
        for j in range(1, i+1) :
            print("{0}*{1}={2} ".format(i,j,j*i))
        print()

string="abcdef"
#print(reverse2(string))
#print(encrypt(string))
#print(Fibon(12))
Multiple_table()
