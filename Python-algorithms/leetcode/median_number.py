class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        new_list = sorted(nums1)
        length = len(new_list)
        if length % 2 == 0:
            return (new_list[length // 2 - 1] + new_list[length // 2]) / 2
        else:
            return new_list[length // 2]


if __name__ == '__main__':
    s_obj = Solution()
    res = s_obj.findMedianSortedArrays([1, 2], [3, 4])
    print(res)
