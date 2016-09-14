#!/usr/bin/env python

def encrypt(a):
    return chr(ord(a)+3)


def encryptA(a):
    b=list(a)
    c=list()
    for i in b:
        c.append(encrypt(i))
    return "".join(c)

def encryptB(a):
    b=""
    for i in a:
        b+=encrypt(i)
    return b

a="ABC"
print "Input :"+a
print "Solution A: Ouput:"+encryptA(a)
print "Solution B: Ouput:"+encryptB(a)
