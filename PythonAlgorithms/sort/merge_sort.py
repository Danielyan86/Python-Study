# 归并排序，递归实现，核心思想：分而治之

def merge_sort(num_l: list):
    length = len(num_l)
    if length <= 1:
        return num_l
    else:
        l_nums = merge_sort(num_l[0:length // 2])
        r_nums = merge_sort(num_l[length // 2:])
        templ_list = []
        while l_nums and r_nums:
            if l_nums[0] < r_nums[0]:
                templ_list.append(l_nums[0])
                del l_nums[0]
            else:
                templ_list.append(r_nums[0])
                del r_nums[0]
        if l_nums:
            templ_list.extend(l_nums)
        if r_nums:
            templ_list.extend(r_nums)
        return templ_list


if __name__ == '__main__':
    res = merge_sort([1, 2, 3, 4])
    print(res)
