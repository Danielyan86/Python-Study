# 题目，1到9不重复的9个数字，使得三位数加三位数等式成立

import itertools
import time

# 暴力穷举算法, 此方法效率极低，需要半个多小时
start = time.clock()
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
end = time.clock()
print('Running time: %s Seconds' % (end - start))

start = time.clock()
for num in range(123, 500):
    for num2 in range(123, 500):
        add_result = num + num2
        all_num_string = "{0}{1}{2}".format(num, num2, add_result)
        flag = True
        if add_result < 1000:
            for j in range(1, 10):  # 判断有没有重复的数字
                if str(j) not in all_num_string:
                    flag = False
                    break
        if flag:
            print("{0}+{1}={2}".format(num, num2, add_result))
end = time.clock()
print('Running time: %s Seconds' % (end - start))

start = time.clock()
# 优化后的方案采用全排列的思想, 大大执行提高效率
for item in itertools.permutations("123456789", 9):  # 全排列方法permutations
    number_string = "".join(item)  # 字符串转化成列表
    if int(number_string[0:3]) + int(number_string[3:6]) == int(number_string[6:]) and int(number_string[0:3]) < 500:
        print("{0}+{1}={2}".format(number_string[0:3], number_string[3:6], number_string[6:]))
end = time.clock()
print('Running time: %s Seconds' % (end - start))
