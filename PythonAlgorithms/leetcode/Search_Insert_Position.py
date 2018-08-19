class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            if target < nums[0]:
                return 0
            for index, num in enumerate(nums):
                if target < num:
                    return index
            return index + 1


if __name__ == '__main__':
    s_obj = Solution()
    res = s_obj.searchInsert([1, 3, 5, 6], 2)
    print(res)
