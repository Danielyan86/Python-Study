#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Reverse(object):
    def reverse(self, text):
        if len(text) <= 1:
            return text
        return self.reverse(text[1:]) + text[0]

    def run(self):
        print self.reverse('ABC')

if __name__ == '__main__':
	e = Reverse()
	e.run()

