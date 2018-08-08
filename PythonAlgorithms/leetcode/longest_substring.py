import time


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # s_length, longest_substr_length = len(s), len(set(s))
        # if longest_substr_length == s_length:
        #     return s_length
        # elif longest_substr_length < s_length:
        #     temporary = 0
        #     for j in range(0, s_length - longest_substr_length + 1):
        #         if len(set(s[j:j + longest_substr_length])) == longest_substr_length:
        #             return longest_substr_length
        #         elif len(set(s[j:j + longest_substr_length])) < longest_substr_length:
        #             sub_res = self.lengthOfLongestSubstring(s[j:j + longest_substr_length])
        #             if sub_res > temporary:
        #                 temporary = sub_res
        #     return temporary
        # 存储历史循环中最长的子串长度
        max_len = 0
        # 判断传入的字符串是否为空
        if s is None or len(s) == 0:
            return max_len
        # 定义一个字典，存储不重复的字符和字符所在的下标
        str_dict = {}
        # 存储每次循环中最长的子串长度
        one_max = 0
        # 记录最近重复字符所在的位置+1
        start = 0
        for i in range(len(s)):
            # 判断当前字符是否在字典中和当前字符的下标是否大于等于最近重复字符的所在位置
            if s[i] in str_dict and str_dict[s[i]] >= start:
                # 记录当前字符的值+1
                start = str_dict[s[i]] + 1
            # 在此次循环中，最大的不重复子串的长度
            one_max = i - start + 1
            # 如果是新字符，添加到字典，如果是已经存在的字符，把当前位置覆盖字典中的位置
            str_dict[s[i]] = i
            # 比较此次循环的最大不重复子串长度和历史循环最大不重复子串长度
            max_len = max(max_len, one_max)
        return max_len


if __name__ == '__main__':
    start = time.clock()
    s_obj = Solution()
    print(s_obj.lengthOfLongestSubstring("hwwsueopsgokfmivjbeppgreozwuud"))

    end = time.clock()
    print('Running time: %s Seconds' % (end - start))
