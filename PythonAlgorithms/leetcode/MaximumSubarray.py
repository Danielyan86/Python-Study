# 题目： 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 求和，然后判断和是否小于0，因为只要前面的和小于0，那么后面的数加上前面的和就一定比自身小，所以又重新求和，
# 并和之前的最大子序和比较，取最大值。
# 思维盲点：负数越加越少
# 推导过程，从一个数，两个数情况开始推导

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sub_sum, max_sum = 0, 0-
        for num in nums:
            if sub_sum >= 0:
                sub_sum = sub_sum + num
            else:
                sub_sum = num
            max_sum = max(max_sum, sub_sum)
        return max_sum


if __name__ == '__main__':
    s_obj = Solution()
    res = s_obj.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(res)
