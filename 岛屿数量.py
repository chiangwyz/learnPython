"""
这个问题的核心是计算二维网格中岛屿的数量。
岛屿定义为由相邻的陆地（'1'）构成的区域，且被水（'0'）包围。
为了找到所有的岛屿，我们可以使用深度优先搜索（DFS）算法。具体步骤如下：

1. 遍历网格中的每个单元格。
2. 当遇到一个值为 '1' 的单元格时，将其视为岛屿的一部分，然后进行深度优先搜索，以标记所有与之相连的陆地（'1'）。
3. 在DFS过程中，将访问过的陆地单元格标记为 '0'，以避免重复计算。
4. 对于每次在DFS中找到的相连陆地区域，岛屿数量加一。
5. 继续遍历直到网格中的所有单元格都被检查过。
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def dfs(i, j):
            # 超出边界或者当前单元格为'0'（水或已访问的陆地）
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return
            # 将当前陆地标记为已访问
            grid[i][j] = '0'  
            # 向四个方向进行深度优先搜索
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0  # 岛屿数量
        # 遍历每个单元格
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 发现一个新岛屿
                if grid[i][j] == '1':
                    dfs(i, j)  # 进行DFS并标记所有相连的陆地
                    count += 1  # 岛屿数量加一

        return count

# 示例使用
solution = Solution()
grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
print(solution.numIslands(grid1))  # 输出: 1

grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(solution.numIslands(grid2))  # 输出: 3




