class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 3:
            return sum(nums)
        nums = sorted(nums)
        difference_num = float("inf")
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i - 1]:
                left_point = i + 1  # 指针每次不用从第一个开始，因为加法交换律
                right_point = len(nums) - 1
                while left_point < right_point:
                    three_sum = nums[i] + nums[left_point] + nums[right_point]
                    res = three_sum - target
                    if res == 0:
                        return three_sum
                    elif res < 0:
                        if abs(res) < difference_num:  # 判定更新结果条件
                            result_return = three_sum
                        left_point += 1
                    elif res > 0:
                        if abs(res) < difference_num:
                            result_return = three_sum
                        right_point -= 1
                    difference_num = min(abs(res), difference_num)
        return result_return


if __name__ == '__main__':
    nums = [0,2,1,-3]
    s_obj = Solution()
    print(s_obj.threeSumClosest(nums, 1))
