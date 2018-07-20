import re


class Solution:
    def myAtoi(self, str_p):
        """
        :type str: str
        :rtype: int
        """
        over_number = pow(2, 31)
        pattern = re.compile(r"(\d+)")
        str_p = str_p.strip()
        if str_p.startswith("-"):
            str_p = str_p[1:]
            res = pattern.match(str_p)
            if res:
                number_str = res.group()
                number_ret = int(number_str)
                return 0 - over_number if number_ret > over_number else 0 - number_ret
            else:
                return 0
        else:
            if str_p.startswith("+"):
                str_p = str_p[1:]
            res = pattern.match(str_p)
            if res:
                number_str = res.group()
                number_ret = int(number_str)
                return over_number - 1 if number_ret > over_number - 1 else number_ret
            else:
                return 0


if __name__ == '__main__':
    s_obj = Solution()
    res = s_obj.myAtoi("+1")
    print(res)
