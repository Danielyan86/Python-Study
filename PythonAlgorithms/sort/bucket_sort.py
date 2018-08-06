import random


# produce the random number list
def produce_random_number(num):
    number_list = []
    for i in range(0, num):
        number_list.append(random.randint(0, 100))
    return number_list


def bucket_sort(original_num):
    bucket_numbers = max(original_num)
    new_list = []
    bucket_dic = {x: x * 0 for x in range(0, bucket_numbers + 1)}
    for num in original_num:
        bucket_dic[num] = bucket_dic[num] + 1
    for num in range(0, bucket_numbers + 1):
        if bucket_dic[num] != 0:
            for j in range(0, bucket_dic[num]):
                new_list.append(num)
    return new_list

if __name__ == '__main__':
    numbers = produce_random_number(20)
    print bucket_sort(numbers)
