"""
Created on 2013-3-10

@author: xiaodong
"""
import Problem3_Largest_prime_factor
import problem1


def Summation_of_primes(num):
    Myobject = Problem3_Largest_prime_factor.Prime()
    prime_list = Myobject.Prime_list(num)
    Myobject1 = problem1.Multiples()
    sum = Myobject1.Sum_list(prime_list)
    return sum


if __name__ == "__main__":
    num = 2000000
    Summation_of_primes(num)
