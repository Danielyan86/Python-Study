# 快速排序，采取递归方法实现
# 核心思想：找出标杆，递归比较
from random import randrange

number_list = []
base_position = 0


def switch_number(number1, number2):
    number_list[number1], number_list[number2] = number_list[number2], number_list[number1]


def quciksort(left_num, right_num):
    if left_num > right_num:
        return

    base_number_value = number_list[left_num]
    base_number = left_num
    left_soldier = left_num
    right_soldier = right_num

    while left_soldier != right_soldier:
        while (number_list[right_soldier] >= base_number_value) and (right_soldier > left_soldier):
            right_soldier = right_soldier - 1

        while (number_list[left_soldier] <= base_number_value) and (right_soldier > left_soldier):
            left_soldier = left_soldier + 1

        if right_soldier > left_soldier:
            switch_number(left_soldier, right_soldier)

    switch_number(base_number, left_soldier)
    quciksort(left_num, left_soldier - 1)
    quciksort(left_soldier + 1, right_num)


# more elegant solution
def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        return qsort([x for x in arr[1:] if x < pivot]) + [pivot] + qsort([x for x in arr[1:] if x >= pivot])


if __name__ == "__main__":
    # This is is used for producing test data
    for time in range(10):
        number_list.append(randrange(1, 10000))
    print("original list:", number_list)
    print("sorted list:", qsort(number_list))
    # quciksort(0, len(number_list) - 1)

    # print "new list after quicksort:", number_list
