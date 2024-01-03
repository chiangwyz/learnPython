"""
使用动态规划求解，定义数组dp
dp[i][j] 表示为从左上角到第i行第j列的最小总和。
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        # dp[i][j] 表示为从左上角到第i行第j列的最小总和。
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        # 首个元素的总和就是其本身
        dp[0][0] = grid[0][0]

        # 初始化第一列
        for i in range(1, rows):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        # 初始化第一行
        for j in range(1, cols):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        # 填充剩下的单元格
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[rows-1][cols-1]
