#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Multiple(object):
    def print_table(self, n):
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print "{0} x {1} = {2}".format(j, i, j * i),
            print ""

    def run(self):
        while True:
            number = raw_input('Enter a number for printing multiple table:')
            if len(number) < 1:
                print "number can't be empty"
            else:
                self.print_table(int(number))
                exit()


if __name__ == '__main__':
    m = Multiple()
    m.run()
