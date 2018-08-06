class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        import re
        result = re.fullmatch(p, s)
        if result:
            return True
        return False


if __name__ == '__main__':
    s_obj = Solution()
    print(s_obj.isMatch(s="aa", p="a"))
