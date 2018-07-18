class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) > 0:
            if s == s[::-1]:
                return s
            for i in range(len(s) - 1, 0, -1):
                for j in range(0, len(s) - i + 1):
                    sub_str = s[j:j + i]
                    if sub_str == sub_str[::-1]:
                        return sub_str


if __name__ == '__main__':
    s_obj = Solution()
    res = s_obj.longestPalindrome("abcda")
    print(res)
