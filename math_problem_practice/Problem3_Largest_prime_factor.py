#Largest prime factor
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

class Prime(object):
    
    #judge the is prime
    def Judge_prime(self, num):
        prime_flag = 1
        i = 2
        while i < num**0.5 + 1:
            if num % i == 0:
                prime_flag = 0
                break
            i = i + 1
        if prime_flag == 1:
            return True
        else:
            return False
        
    def Prime_list(self, num):
        list_prime = [2,3]
        for i in range(4, num+1):
            if self.Judge_prime(i):
                list_prime.append(i)
        print 'prime list is %s' % list_prime
        return list_prime
    
    def Devide_prime_list(self, Prime_list, num):
        devide_prime_list=[]
        for i in Prime_list:
            if i <= num/2:
                if num % i == 0:
                    devide_prime_list.append(i)
        print 'devided prime list is %s' % devide_prime_list
        return devide_prime_list
                    
    def Find_largest_prime(self,num):
        i = 2
        while True:
            if num % i == 0:
                new_num = num/i
                if self.Judge_prime(new_num):
                    break
            i = i + 1
        print 'the largest prime is %d' % new_num
        return new_num

if __name__ == '__main__':
    num = 26000001
    myObject = Prime()
#    new_list = myObject.Prime_list(num)
#    print myObject.Devide_prime_list(new_list, num)
    myObject.Find_largest_prime(num)