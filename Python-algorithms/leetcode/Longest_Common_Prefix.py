class Solution:
    def longestCommonPrefix_v1(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) > 0:
            strs = list(set(strs))
            longest_common_prefix = strs[0]
            length = len(strs)
            for i in range(1, length):
                if strs[i].startswith(longest_common_prefix):
                    continue
                else:
                    if longest_common_prefix:
                        strs_c = strs[i]
                        min_len = min(len(strs_c), len(longest_common_prefix))
                        new_prefix = ""
                        for j in range(0, min_len):
                            if strs_c[j] == longest_common_prefix[j]:
                                new_prefix = "".join((new_prefix, strs_c[j]))
                            else:
                                break
                        longest_common_prefix = new_prefix
                    else:
                        break
            return longest_common_prefix
        else:
            return ""

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        strs = list(set(strs))
        shortest = min(strs, key=len)
        for x, y in enumerate(shortest):
            for s in strs:
                if s[x] != y:
                    return shortest[:x]
        return shortest

    def longestCommonPrefix_improved(self, strs):
        if len(strs) > 0:
            strs = list(set(strs))
            shortest = min(strs, key=len)  # 找出列表中的最短字符串
            shortest_len = len(shortest)
            longest_common_prefix = shortest
            length = len(strs)
            for i in range(length):
                if shortest_len:
                    if strs[i].startswith(longest_common_prefix):
                        continue
                    else:
                        shortest_len = shortest_len - 1
                        while shortest_len >= 0:
                            if strs[i].startswith(longest_common_prefix[:shortest_len]):
                                longest_common_prefix = longest_common_prefix[:shortest_len]
                                break
                            shortest_len = shortest_len - 1
                else:
                    return ""
            return longest_common_prefix
        else:
            return ""


if __name__ == '__main__':
    s_obj = Solution()
    res = s_obj.longestCommonPrefix_improved(["flower", "flow", "flight"])
    print(res)
