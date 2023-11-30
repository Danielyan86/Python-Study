"""
Created on 2013-3-1

@author: xiaodong
"""
import Problem3_Largest_prime_factor


def Find_N_prime(num):
    myObject = Problem3_Largest_prime_factor.Prime()
    prime_list = [2, 3]
    i = 4
    while len(prime_list) < num:
        if myObject.Judge_prime(i):
            prime_list.append(i)
        i = i + 1
    return prime_list


if __name__ == "__main__":
    num = 10001
    print
    Find_N_prime(num)
