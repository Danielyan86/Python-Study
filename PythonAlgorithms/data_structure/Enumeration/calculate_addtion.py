# 题目，1到9不重复的9个数字，使得三位数加三位数等式成立

import itertools
import time


# 优化判断重复数字部分,1~9数字全部必须出现一次
def judge_numbers(number):
    if len(set(str(number))) == 9 and "0" not in str(number):
        return True
    else:
        return False


# 暴力穷举算法, 此方法效率极低，优化前需要半个多小时
def violent_enumeration():
    start = time.clock()
    for number in range(123456789, 150654321):
        # flag = True
        # for j in range(1, 10):  # 判断有没有重复的数字
        #     if str(j) not in str(number):
        #         flag = False
        #         break

        if judge_numbers(number):
            number_string = str(number)
            if (
                int(number_string[0:3]) + int(number_string[3:6])
                == int(number_string[6:])
                and int(number_string[0:3]) < 200
            ):
                print(
                    "{0}+{1}={2}".format(
                        number_string[0:3], number_string[3:6], number_string[6:]
                    )
                )
    end = time.clock()
    print("Running time: %s Seconds" % (end - start))


def optimized_enumeration():
    start = time.clock()
    for num in range(123, 500):
        for num2 in range(123, 500):
            add_result = num + num2
            all_num_string = "{0}{1}{2}".format(num, num2, add_result)
            if judge_numbers(all_num_string):
                print("{0}+{1}={2}".format(num, num2, add_result))
    end = time.clock()
    print("Running time: %s Seconds" % (end - start))


def permutations_fun():
    start = time.clock()
    # 优化后的方案采用全排列的思想, 大大执行提高效率
    for item in itertools.permutations("123456789", 9):  # 全排列方法permutations
        number_string = "".join(item)  # 字符串转化成列表
        if (
            int(number_string[0:3]) + int(number_string[3:6]) == int(number_string[6:])
            and int(number_string[0:3]) < 500
            and int(number_string[3:6]) < 500
            and int(number_string[6:]) < 1000
        ):
            print(
                "{0}+{1}={2}".format(
                    number_string[0:3], number_string[3:6], number_string[6:]
                )
            )
    end = time.clock()
    print("Running time: %s Seconds" % (end - start))


def multiple():
    for i in range(1, 10):
        if int("{0}3".format(i)) * 6528 == int("3{0}".format(i)) * 8256:
            print(i, int("{0}3".format(i)) * 6528)
    print(
        [
            i
            for i in range(1, 10)
            if int("{0}3".format(i)) * 6528 == int("3{0}".format(i)) * 8256
        ]
    )


if __name__ == "__main__":
    # violent_enumeration()
    # optimized_enumeration()
    permutations_fun()
    multiple()
