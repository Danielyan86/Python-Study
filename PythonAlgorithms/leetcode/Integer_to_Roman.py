class Solution:

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # 每一个位数字母组合规律是一样的，比如个位3是III，30则是XXX
        # Roman_dic = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}

        rome_str = ""
        lable = 1
        if num > 0 and num < 4000:
            while num != 0:
                res = num % 10
                rome_str = self.convert_num_into_rome_letter(res, lable) + rome_str
                num = num // 10
                lable = lable + 1
        print(rome_str)
        return rome_str

    def convert_num_into_rome_letter(self, num, lable):
        Roman_dic = {1: ["I", "V", "X"], 2: ['X', 'L', 'C'], 3: ['C', 'D', 'M'], 4: ['M']}
        num_list = Roman_dic[lable]
        if num < 4:
            return num * num_list[0]
        elif num == 4:
            return num_list[0] + num_list[1]
        elif num == 5:
            return num_list[1]
        elif num < 9:
            return num_list[1] + (num - 5) * num_list[0]
        elif num == 9:
            return num_list[0] + num_list[2]

if __name__ == '__main__':
    s_obj = Solution()
    s_obj.intToRoman(1994)