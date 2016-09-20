#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Multiple_Table(object):
    def multiple_table(self, number1):

        for i in range(1, number1):
            for j in range(1, i + 1):
                a = i * j
                # 输出和预期不符，如何解决？
                print "{0} x {1} = {2}".format(j, i, j * i),
            print ""

    def run(self):
        number = int(input('Enter a number for printing multiple table:'))
        if number < 1:
            print 0
        self.multiple_table(number)


if __name__ == '__main__':
	e = Multiple_Table()
	e.run()