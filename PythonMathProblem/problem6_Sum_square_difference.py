'''
Created on 2013-2-26

@author: xiaodong
'''


def Sum_Square_Difference(num):
    list = []
    for i in range(1, num + 1):
        difference = Sum_and_square(i) - Squar_and_sum(i)
        list.append(difference)
    return list


def Squar_and_sum(num):
    sum = 0
    for i in range(1, num + 1):
        sum = sum + i * i
    return sum


def Sum_and_square(num):
    sum = 0
    for i in range(1, num + 1):
        sum = sum + i
    sum = sum * sum
    return sum


if __name__ == '__main__':
    num = 100
    difference = Sum_and_square(num) - Squar_and_sum(num)
    print
    difference
