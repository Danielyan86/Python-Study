#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Fibonacci(object):

    def recur_fibo(self, n):
        if n <= 1:
            return n
        else:
            return self.recur_fibo(n - 1) + self.recur_fibo(n - 2)

    def run(self):
        nterms = int(input("您要输出几项? "))
        if nterms <= 0:
            print("输入正数")
        else:
            print("斐波那契数列:")
            for i in range(nterms):
                print(self.recur_fibo(i))



if __name__ == '__main__':
	e = Fibonacci()
	e.run()