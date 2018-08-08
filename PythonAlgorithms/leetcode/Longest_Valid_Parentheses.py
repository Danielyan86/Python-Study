class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        # @param s, a string
        # @return an integer
        longest, last, indices = 0, -1, []
        for i in range(len(s)):
            if s[i] == '(':
                indices.append(i) #存入索引值
            elif not indices:
                last = i
            elif s[i] == ')':
                indices.pop()
                if not indices:
                    longest = max(longest, i - last)
                else:
                    longest = max(longest, i - indices[-1])
        return longest


if __name__ == '__main__':
    s_obj = Solution()
    res = s_obj.longestValidParentheses("(()())")
    print(res)
