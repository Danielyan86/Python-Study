# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        for i in range(1, length):
            # 当前值的大小与前面的值之和比较，若当前值更大，则取当前值，舍弃前面的值之和
            subMaxSum = max(nums[i] + nums[i - 1], nums[i])
            nums[i] = subMaxSum  # 将当前和最大的赋给nums[i]，新的nums存储的为和值
        return max(nums)


if __name__ == '__main__':
    s_obj = Solution()
    res = s_obj.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(res)
