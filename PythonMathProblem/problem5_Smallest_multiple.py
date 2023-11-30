"""
Created on 2013-2-26

@author: xiaodong
"""
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import Problem3_Largest_prime_factor
import problem1


def Smallest_multiple(num):
    P3object = Problem3_Largest_prime_factor.Prime()
    P1object = problem1.Multiples()

    prime_list = P3object.Prime_list(num)
    sum = P1object.Multiple_list(prime_list)

    print
    "Smallest multiple is %d" % sum
    return sum


if __name__ == "__main__":
    num = 10
    print
    Smallest_multiple(num)
