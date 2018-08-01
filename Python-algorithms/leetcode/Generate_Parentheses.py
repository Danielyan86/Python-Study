class Solution:

    # 此题是生成一个包含字符串的的list，生成一个由括号组成的字符串完全可以增益方式生成
    # 每次递归调用函数时候传入之前的字符串，之前掉入了靠函数返回字符来拼接字符串的误区
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        self.generateParenthesisIter('', n, n)
        return self.res

    def generateParenthesisIter(self, mstr, r, l):
        if r == 0 and l == 0:
            self.res.append(mstr)
        if l > 0:
            self.generateParenthesisIter(mstr + '(', r, l - 1)
        if r > 0 and r > l:
            self.generateParenthesisIter(mstr + ')', r - 1, l)


if __name__ == '__main__':
    s_obj = Solution()
    res = s_obj.generateParenthesis(3)
    print(res)
