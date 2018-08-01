class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while True:
            if val in nums:
                nums.remove(val)
            else:
                break
        return len(nums)


if __name__ == '__main__':
    s_obj = Solution()
    print(s_obj.removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))
