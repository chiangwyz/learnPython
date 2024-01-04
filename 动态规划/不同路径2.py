"""
使用一个二维数组 dp 来存储从起点到达网格的每一个点的路径数。由于机器人只能向下或者向右移动，
因此到达每一个点的路径数是它上方点和左方点的路径数之和。但是，如果某个点有障碍物，那么到达这个点的路径数就是 0。

1. 初始化 dp 数组：首先，我们需要初始化一个和输入网格大小相同的 dp 数组。所有元素初始值设为 0。
2. 处理起点：如果起点即 obstacleGrid[0][0] 有障碍物，则返回 0，因为没有路径可以到达终点。否则，设置 dp[0][0] 为 1，表示起点。
3. 填充 dp 数组：遍历整个网格，对于每个点：
  如果这个点有障碍物，则 dp[i][j] = 0。
  如果这个点没有障碍物，则 dp[i][j] = dp[i-1][j] + dp[i][j-1]。需要注意边界条件，即如果 i 或 j 为 0，那么 dp[i-1][j] 或 dp[i][j-1] 可能不存在。
4. 返回结果：dp[m-1][n-1] 就是从左上角到右下角的路径总数。
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 如果起点有障碍物，则无法到达终点
        if not obstacleGrid:
            return 0

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp = [[0]*cols for _ in range(rows)]
        dp[0][0] = 1

        for i in range(rows):
            for j in range(cols):
                if obstacleGrid[i][j] == 1:
                    # 如果有障碍物，则路径数为0
                    dp[i][j] = 0  
                else:
                    if i > 0:
                        # 加上从上方来的路径数
                        dp[i][j] += dp[i-1][j]  
                    if j > 0:
                        # 加上从左方来的路径数
                        dp[i][j] += dp[i][j-1]  

        # 返回终点的路径数
        return dp[rows-1][cols-1]  
