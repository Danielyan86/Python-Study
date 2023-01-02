'''
Created on 2013-2-26

@author: xiaodong
'''
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def Largest_Palindrome_Product(num_digit):
    max = 0
    for i in range(1, num_digit):
        for j in range(i, num_digit):
            sum = i*j
            if str(sum) == str_reverse(str(sum)):
                if sum > max:
                    num1 = i
                    num2 = j
                    max = sum
    print "max is %d by %d * %d" % (max, num1, num2)                 
    return max

#reverse the string
def str_reverse(str):
    length = len(str)
    new_string = ''
    for i in range(length-1, -1, -1):
        new_string = new_string + str[i]
#        print new_string
    return new_string

if __name__ == '__main__':
    num_digit = 1000
    print Largest_Palindrome_Product(num_digit)
