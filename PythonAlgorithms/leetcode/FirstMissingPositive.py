class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        smallest_positive = 1
        exist_nums_dic = {}
        for item in nums:
            if item == smallest_positive:
                exist_nums_dic[item] = True
                smallest_positive = smallest_positive + 1
                while smallest_positive in exist_nums_dic:
                    smallest_positive = smallest_positive + 1
            elif item > 0:
                exist_nums_dic[item] = True
        return smallest_positive


if __name__ == '__main__':
    s_obj = Solution()
    res = s_obj.firstMissingPositive(
        [-3, 9, 16, 4, 5, 16, -4, 9, 26, 2, 1, 19, -1, 25, 7, 22, 2, -7, 14, 2, 5, -6, 1, 17, 3, 24, -4, 17, 15])
    print(res)
