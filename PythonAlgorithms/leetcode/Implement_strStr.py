class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack or needle:
            if needle in haystack:
                return haystack.index(needle)
            else:
                return -1
        else:
            return 0


if __name__ == '__main__':
    s_obj = Solution()
    res = s_obj.strStr(haystack="", needle="")
    print(res)
