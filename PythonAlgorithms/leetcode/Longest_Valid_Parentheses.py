class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        Parentheses = []
        length = 0
        max_length = 0
        total_length = 0
        for letter in s:
            if letter == "(":
                if Parentheses:
                    length = 0
                    total_length = total_length + length + 2
                Parentheses.append(letter)
            elif letter == ")":
                if Parentheses:
                    Parentheses.pop()
                    if Parentheses:  # 弹出一个左括号以后如果还有多的左括号，则累加
                        length = length + 2
                    else:  # 如果弹出左括号以后列表为空，则长度清零，单次总长度累加
                        length = 0
                        total_length = total_length + length + 2
                else:
                    length, total_length = 0, 0  # 如果右括号进来没有左括号匹配，则清零，重新计数
            one_max_len = max(length, total_length)
            max_length = max(max_length, one_max_len)
        # max_length = max(max_length, total_length)
        return max_length


if __name__ == '__main__':
    s_obj = Solution()
    res = s_obj.longestValidParentheses("()(()")
    print(res)
