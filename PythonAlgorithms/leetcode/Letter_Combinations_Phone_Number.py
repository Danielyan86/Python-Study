import itertools


class Solution:
    dic_number = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # dic_number = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        digits_len = len(digits)
        if digits_len >= 2:
            letter_list = []
            for i in range(len(self.dic_number[digits[0]])):
                res = self.deep_combinations(digits, i)
                letter_list.extend(res)
            return letter_list
            # return [self.deep_combinations(digits, i) for i in range(len(self.dic_number[digits[0]]))]
        elif digits_len == 1:
            return list(self.dic_number[digits])
        else:
            return []

    def deep_combinations(self, str_num, letter_lable):
        letter_list = []
        if len(str_num) == 1:
            return self.dic_number[str_num][letter_lable]
        else:
            letter = self.dic_number[str_num[0]][letter_lable]
            next_letter_str_len = len(self.dic_number[str_num[1]])
            letter_lable = 0
            while letter_lable < next_letter_str_len:
                res = self.deep_combinations(str_num[1:], letter_lable)
                if isinstance(res, list):
                    letter_list.extend([letter + item for item in res])
                else:
                    letter_list.append(letter + res)
                letter_lable = letter_lable + 1
            return letter_list

        # for num_str in digits_set:
        #     str_res = "".join((str_res, dic_number[num_str]))
        # return ["{0}{1}".format(item[0], item[1]) for item in list(itertools.combinations(str_res, 2))]


if __name__ == '__main__':
    number_string = "234"
    s_obj = Solution()
    print(s_obj.letterCombinations(number_string))
    # print(list(itertools.zip_longest('ABCD', 'xy')))
