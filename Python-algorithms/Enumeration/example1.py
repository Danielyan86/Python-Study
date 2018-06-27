# 题目，1到9不重复的9个数字，使得三位数加三位数等式成立
# 暴力穷举算法, 此方法
for number in range(123456789, 987654321):
    flag = True
    for j in range(1, 10):  # 判断有没有重复的数字
        if str(j) not in str(number):
            flag = False
            break
    if flag:
        number_string = str(number)
        if int(number_string[0:3]) + int(number_string[3:6]) == int(number_string[6:]) and int(
                number_string[0:3]) < 500:
            print("{0}+{1}={2}".format(number_string[0:3], number_string[3:6], number_string[6:]))

# 优化后的方案采用全排列的思想, 大大执行提高效率
import itertools

for item in itertools.permutations("123456789", 9):
    number_string = "".join((item))
    if int(number_string[0:3]) + int(number_string[3:6]) == int(number_string[6:]) and int(number_string[0:3]) < 500:
        print("{0}+{1}={2}".format(number_string[0:3], number_string[3:6], number_string[6:]))
