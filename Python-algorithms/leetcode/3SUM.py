import itertools

nums = [-1, 0, 1, 2, -1, -4]
# print(list(itertools.combinations(num, 3)))

table = []

'''the first method'''
# print(sorted(nums))
# 处理三个零特殊情况
# zero_count = nums.count(0)
# if zero_count >= 3:
#     table.append([0, 0, 0])
#
# new_nums = []
# num_count_dic = {}
# for num in nums:
#     if num in num_count_dic:
#         if num_count_dic[num] == 2:
#             continue
#         else:
#             num_count_dic[num] = num_count_dic[num] + 1
#             new_nums.append(num)
#     else:
#         num_count_dic[num] = 1
#         new_nums.append(num)
#
# sorted_nums = sorted(set(new_nums))  # 列表排序
# # print(sorted_nums)
#
# if zero_count > 0:
#     zero_index = sorted_nums.index(0)
#     minus_list = sorted_nums[0:zero_index]
#     positive_list = sorted_nums[zero_index:]
#     for i in range(0, len(minus_list)):
#         if minus_list[i] + positive_list == 0:
#             table.append([minus_list[i], 0, abs(minus_list[i])])
# for key, value in num_count_dic.items():
#     if value == 2:
#         if key < 0:
#             if abs(key * 2) in sorted_nums:
#                 table.append([key, key, abs(2 * key)])
#         elif key > 0:
#             if 0 - key * 2 in sorted_nums:
#                 table.append([key, key, 0 - 2 * key])
#
# minus_list, positive_list = [], []
# for num in sorted_nums:
#     if num < 0:
#         minus_list.append(num)
#     elif num > 0:
#         positive_list.append(num)
# for item in itertools.combinations(minus_list, 2):
#     add_sum = item[0] + item[1]
#     if abs(add_sum) in positive_list:
#         table.append([item[0], item[1], abs(add_sum)])
# for item in itertools.combinations(positive_list, 2):
#     add_sum = 0 - (item[0] + item[1])
#     if add_sum in minus_list:
#         table.append([item[0], item[1], add_sum])
#
# print(table)

# print(table)
'''The second methods'''

nums.sort()  # 排序
res = []
# i = 0
for i in range(len(nums)):
    if i == 0 or nums[i] > nums[i - 1]:
        left_point = i + 1
        right_point = len(nums) - 1
        while left_point < right_point:
            add_sum = nums[i] + nums[left_point] + nums[right_point]
            if add_sum == 0:
                res.append([nums[i], nums[left_point], nums[right_point]])
                left_point += 1
                right_point -= 1
                while left_point < right_point and nums[left_point] == nums[left_point - 1]:  # 避免相同值
                    left_point += 1
                while right_point > left_point and nums[right_point] == nums[right_point + 1]:
                    right_point -= 1
            elif add_sum > 0:
                right_point -= 1
            else:
                left_point += 1
print(res)
