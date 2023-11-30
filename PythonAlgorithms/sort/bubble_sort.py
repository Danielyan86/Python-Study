# coding=UTF-8
"""冒泡算法:
核心思想：邻居相比，每次让末尾数字归位，看起来像冒泡一样"""

from PythonAlgorithms.sort.bucket_sort import produce_random_number


def bubble_sort(original_num_list):
    num_list = original_num_list
    numbers = len(num_list)
    for i in range(0, numbers - 1):
        for j in range(0, numbers - i - 1):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
    return num_list


if __name__ == "__main__":
    numbers = produce_random_number(30)
    print(numbers)
    print(bubble_sort(numbers))
