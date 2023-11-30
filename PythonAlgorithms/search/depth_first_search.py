# coding=UTF-8
"""深度优先搜索:
核心思想：全排列思想，第一次：把第一个数放入第一个盒子，n放入第n
                第二次：第二个数字放入第一个，
                递归实现
                注意：python对象的深拷贝
"""
import copy

box = [0, 0, 0]
mark = {1: 0, 2: 0}


def dfs(a_list, step):
    if a_list:
        for i in a_list:
            box[step] = i
            left_element_list = copy.deepcopy(a_list)
            left_element_list.remove(i)
            if len(a_list) == 1:
                dfs(left_element_list, step + 1)
            else:
                dfs(left_element_list, step + 1)
    else:
        print(box)
        return


# 迷宫最短路径算法
class Maze(object):
    path = [(0, 0)]
    maze = (
        (0, 0, 0, 1),
        (1, 0, 0, 0),
        (0, 0, 1, 2),
        (1, 0, 0, 0),
    )
    columns = len(maze) - 1
    rows = len(maze[0]) - 1
    print(rows)

    def dfs(self, x, y):
        if self.maze[x][y] != 2:
            if (y + 1 <= self.rows) and (self.maze[x][y + 1] != 1):
                if (x, y + 1) not in self.path:
                    self.path.append((x, y + 1))
                    self.dfs(x, y + 1)
                    self.path.pop()
            if (0 <= x - 1) and (self.maze[x - 1][y] != 1):
                if (x - 1, y) not in self.path:
                    self.path.append((x - 1, y))
                    self.dfs(x - 1, y)
                    self.path.pop()
            if (0 <= y - 1) and (self.maze[x][y - 1] != 1):
                if (x, y - 1) not in self.path:
                    self.path.append((x, y - 1))
                    self.dfs(x, y - 1)
                    self.path.pop()
            if (x + 1 <= self.columns) and (self.maze[x + 1][y] != 1):
                if (x + 1, y) not in self.path:
                    self.path.append((x + 1, y))
                    self.dfs(x + 1, y)
                    self.path.pop()
            return
        else:
            print(self.path)
            # self.path = [(0, 0)]
            return


if __name__ == "__main__":
    # a = [1, 2, 3]
    # dfs(a, 0)
    maze_obj = Maze()
    maze_obj.dfs(0, 0)
