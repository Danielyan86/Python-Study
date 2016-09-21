#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Encrypt(object):
    def encrypt(self, string):
        return "".join(map(lambda x: chr(ord(x) + 3), list(string)))

    def run(self):
        while True:
            string = raw_input('Enter a string for encrypting:')
            if len(string) < 1:
                print "string can't be empty"
            else:
                print self.encrypt(string)
                exit()


if __name__ == '__main__':
    e = Encrypt()
    e.run()
