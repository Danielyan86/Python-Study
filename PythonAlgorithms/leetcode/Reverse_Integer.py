class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str_num = str(x)
        if "-" in str_num:
            str_num = str_num[1:]
            res_int = int(str_num[::-1])
            return 0 if res_int > pow(2, 31) else 0 - res_int
        else:
            res_int = int(str_num[::-1])
            return 0 if res_int > pow(2, 31) - 1 else res_int

    def reverse_v2(self, x):
        """
        :type x: int
        :rtype: int
        """
        str_num = str(x)
        over_nubmer = pow(2, 31)  # 优先计算出over_number的值, 大大提升执行料率
        if "-" in str_num:
            str_num = str_num[1:]
            res_int = int("".join(reversed(str_num)))
            return 0 if res_int > over_nubmer else 0 - res_int
        else:
            res_int = int("".join(reversed(str_num)))
            return 0 if res_int > over_nubmer - 1 else res_int


if __name__ == '__main__':
    s_obj = Solution()
    # res = s_obj.reverse("-123")
    res = s_obj.reverse_v2("-123")
    print(res)
