class Solution:
    def convert_old(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # 根据题目给出的z形状的规则构建一个二维数组，在按照要求输出字符串
        if numRows == 1:
            return s

        table = []
        colume = 0
        while True:
            if colume % (numRows - 1) == 0:
                if numRows <= len(s):
                    line = list(s[0:numRows])
                    s = s[numRows:]
                    if not s:
                        table.append(line)
                        break
                elif numRows > len(s):
                    line = list(s[0:len(s)])
                    line = line + [""] * (numRows - len(s))
                    table.append(line)
                    break
                colume = colume + 1
                single_letter_position = numRows - 2
                table.append(line)
            else:
                line = [""] * numRows
                line[single_letter_position] = s[0]
                if s[1:]:
                    s = s[1:]
                    colume = colume + 1
                    table.append(line)
                    single_letter_position = single_letter_position - 1
                else:
                    table.append(line)
                    break
        for line in table:
            print(line)
        res_s = ""
        for i in range(numRows):
            for line in table:
                res_s = res_s + line[i]
        return res_s

    def convert(self, s, numRows):
        if numRows == 1:
            return s
        res_s = ""
        str_len = len(s)

        for i in range(0, numRows):
            start_p = i  # 每一行第一个字符输出位置
            position = 0
            print(res_s)
            while True:
                if i == 0 or i == numRows - 1:
                    print(start_p)

                    res_s = res_s + s[start_p]
                    start_p = start_p + numRows * 2 - 2
                    if start_p >= str_len:
                        break
                else:
                    res_s = res_s + s[start_p]
                    if i <= str_len // 2:
                        if position % 2 == 0:  # 偶数位和奇数位不一样
                            start_p = start_p + (numRows - (i + 1)) * 2
                        else:
                            start_p = start_p + 2 * i
                        position = position + 1
                    elif i > str_len // 2:
                        if position % 2 != 0:  # 偶数位和奇数位不一样
                            start_p = start_p + (numRows - (i + 1)) * 2
                        else:
                            start_p = start_p + 2 * i
                        position = position + 1
                    if start_p >= str_len:
                        break
        return res_s


if __name__ == '__main__':
    s_obj = Solution()
    res = s_obj.convert("PAYPALISHIRING", 3)
    print(res)
