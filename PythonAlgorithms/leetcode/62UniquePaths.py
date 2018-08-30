# 题目：一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 问总共有多少条不同的路径？

# 思路：迷宫问题，可以用搜索算法解答，广度优先搜索或者深度优先搜索
# 提交过后发现运算超时


# 动态规划就是解决了重复计算，具体实现方式有：
# 记忆化搜索
# 循环求解(本题采用此方法)
# 典型DP问题 - 矩阵型动态规划(Matrix DP)
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 初始化一个值全为1的矩阵，这样可以不用再去给边界赋值
        path_martrix = [[1 for i in range(m)] for j in range(n)]
        for line in range(1, n):  # 从第二行第二列开始遍历矩阵
            for col in range(1, m):
                path_martrix[line][col] = path_martrix[line - 1][col] + path_martrix[line][col - 1]  # 推导式
        return path_martrix[n - 1][m - 1]  # 返回矩阵最右下角的值


class Solution2:
    counter = 0

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        if m != 1 and n != 1:
            self.uniquePaths(m - 1, n)
            self.uniquePaths(m, n - 1)
        if m == 1 or n == 1:
            self.counter = self.counter + 1
            return


if __name__ == '__main__':
    s_obj = Solution()
    res = s_obj.uniquePaths(3, 2)
    print(res)
