class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(0, length - 1):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == '__main__':
    sum_obj = Solution()
    print(sum_obj.twoSum([2, 11, 7, 12, 13], target=10))
