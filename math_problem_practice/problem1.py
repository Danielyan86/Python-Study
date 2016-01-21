#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
#The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

class Multiples(object):
    
    def Multiples_three_and_five(self, num):
        num_list =[]
        for i in range(1,num):
            if i % 3 == 0:
                num_list.append(i)
            elif i % 5 == 0:
                num_list.append (i)
        return num_list
    
    def Sum_list(self,Num_list):
        sum = 0
        for i in Num_list:
            sum = i + sum
        print 'sum of the list is %d' % (sum)
        return sum
    
    def Multiple_list(self, Num_list):
        result = 1
        for i in Num_list:
            result = i * result
        print 'multiple of the list is %d' % result
        return result
    
if __name__ == '__main__':
    num = 1000
    Myobject = Multiples()
    Num_list = Myobject.Multiples_three_and_five(num)

    print Myobject.Sum_list(Num_list)