class Solution:
    def maxArea_violent(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        height = [0] + height
        length = len(height)
        max_water_container = 0
        if length >= 2:
            for i in range(0, length - 1):
                for j in range(i + 1, length):
                    hight_min = min(height[i], height[j])
                    max_water_container = max(max_water_container, hight_min * (j - i))
            return max_water_container
        else:
            return 0

    def maxArea(self, height):
        max_area = 0
        height = [0] + height
        length = len(height)
        left_pointer, right_pointer = 1, length - 1
        if length >= 2:
            while left_pointer < right_pointer:
                max_area = max(min(height[left_pointer], height[right_pointer]) * (right_pointer - left_pointer),
                               max_area)
                if height[left_pointer] < height[right_pointer]:
                    left_pointer = left_pointer + 1
                else:
                    right_pointer = right_pointer - 1
        return max_area


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    # height = [1, 1]
    s_obj = Solution()
    res = s_obj.maxArea(height)
    print(res)
