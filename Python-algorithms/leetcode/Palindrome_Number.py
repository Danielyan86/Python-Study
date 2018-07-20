class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x < 10 or x == 0:
            return True
        else:
            new_num = x % 10
            x = x // 10
            if new_num == 0:
                return False
            while True:
                if new_num >= x:
                    return new_num == x or new_num // 10 == x  # 表达式本省是否成立可以返回True/False, 不用显示返回
                else:
                    new_num = new_num * 10 + x % 10
                    x = x // 10


if __name__ == '__main__':
    s_obj = Solution()
    print(s_obj.isPalindrome(1233321))
