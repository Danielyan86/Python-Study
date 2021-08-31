# 选择排序（Selection sort）是一种简单直观的排序算法。
# 它的工作原理是每一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，直到全部待排序的数据元素排完。
# 选择排序是不稳定的排序方法。

def sort_selection(nums_list):
    for i in range(len(nums_list) - 1):
        min = i  # 假下标为i的首元素为最小值
        for j in range(i + 1, len(nums_list)):  # 遍历剩下的元素跟当前元素比较
            if (nums_list[j] < nums_list[min]):  # 如果有跟小的值，则更新最下值下标
                min = j
        if min != i:  # 如果min没有更新，则说明值索引i对应值已经是最小的，则不用交换
            nums_list[i], nums_list[min] = nums_list[min], nums_list[i]
    print(nums_list)


if __name__ == '__main__':
    sort_selection([1, 2, 3, 0, -1])
