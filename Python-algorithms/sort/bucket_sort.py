import random


#produce the random number list
def produce_random_number(num):
    number_list = []
    for i in range(0, num):
        number_list.append(random.randint(0, 100))
    return number_list


def bucket_sort(original_num):
    buckets = {}
    sorted_num = []
    for i in range(0, 101):
        buckets[i] = 0
    print "original number list:", original_num
    for num in original_num:
        buckets[num] += 1

    for i in range(0, 101):
        if buckets[i] != 0:
            for j in range(0, buckets[i]):
                sorted_num.append(i)

    return sorted_num

if __name__ == '__main__':
    numbers = produce_random_number(20)
    print bucket_sort(numbers)