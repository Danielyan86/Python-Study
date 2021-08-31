# 归并排序，递归实现，核心思想：分而治之

def merge_sort(num_l: list):
    length = len(num_l)
    if length <= 1:
        return num_l
    else:
        l_nums = merge_sort(num_l[0:length // 2])
        r_nums = merge_sort(num_l[length // 2:])
        temp_list = []
        while l_nums and r_nums:
            if l_nums[0] < r_nums[0]:
                temp_list.append(l_nums[0])
                del l_nums[0]
            else:
                temp_list.append(r_nums[0])
                del r_nums[0]
        if l_nums:
            temp_list.extend(l_nums)
        if r_nums:
            temp_list.extend(r_nums)
        return temp_list


def test_merge_sort():
    res = merge_sort([1, 2, 3, 4])
    assert res == [1, 2, 3, 4]
    assert [1, 2, 3, 4] == merge_sort([4, 3, 2, 1])
    assert [-4, 1, 2, 3, ] == merge_sort([-4, 3, 2, 1])
    assert [1, 1, 3, 3, 4] == merge_sort([4, 3, 3, 1, 1])


if __name__ == '__main__':
    res = merge_sort([1, 2, 3, 4])
    print(res)
