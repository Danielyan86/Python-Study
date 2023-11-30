# 二分法查找，采用递归思想实现
def binary_search(number_list, number):
    length = len(number_list)
    if length == 1:
        return number_list[0]
    elif length == 2:
        return number_list[0] if number_list[0] == number else number_list[1]
    elif length > 2:
        if number > number_list[length // 2]:
            return binary_search(number_list[length // 2 :], number)
        elif number == number_list[length // 2]:
            return number_list[length // 2]
        else:
            return binary_search(number_list[0 : length // 2], number)


if __name__ == "__main__":
    number_list, number = list(range(1000000)), 3334
    print(binary_search(number_list, number))
