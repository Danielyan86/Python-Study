import itertools

table = []
for item in itertools.permutations([1, 2, 3], 3):
    table.append(item)
print(table)

print(list(itertools.permutations([1, 2, 3], 3)))


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        return [item for item in itertools.permutations(nums, length)]