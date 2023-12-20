"""
要解决这个问题，我们可以采用动态规划的方法。动态规划是解决这类问题的一个有效工具，因为它可以帮助我们将大问题分解为较小的子问题，并存储中间结果以避免重复计算。

在这个特定的问题中，我们的目标是找到只包含 '1' 的最大正方形的面积。
我们可以通过遍历矩阵，对于每一个点，计算以它为右下角的最大正方形的边长。
这个边长可以通过查看它的左边、上边和左上角的点的最大边长来确定。

我们定义一个与原矩阵同样大小的dp矩阵，dp[i][j]代表以matrix[i][j]为右下角的最大正方形的边长。
对于矩阵中的每一个点，如果它是'1'，那么dp[i][j]的值至少是1。
如果它的左边、上边和左上角也都是'1'，那么dp[i][j]就可以根据这些点的dp值加
""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        max_side = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    # 如果是矩阵的第一行或第一列，那么最大边长就是1
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        # 否则，取决于它的左边、上边和左上角的最小值
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_side = max(max_side, dp[i][j])
        
        # 返回最大正方形的面积
        return max_side ** 2





