class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p_list = []
        for letter in s:
            if letter in '({[':
                p_list.append(letter)
            else:
                if p_list:
                    if letter == ')':
                        if p_list.pop() != '(':
                            return False
                    elif letter == ']':
                        if p_list.pop() != '[':
                            return False
                    elif letter == '}':
                        if p_list.pop() != '{':
                            return False
                else:
                    return False
        return False if p_list else True


if __name__ == '__main__':
    parenthesis = "{[]}"
    s_obj = Solution()
    res = s_obj.isValid(parenthesis)
    print(res)
