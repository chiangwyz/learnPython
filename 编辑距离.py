"""
在这个问题中，我们将创建一个二维数组 dp，其中 dp[i][j] 表示将 word1 的前 i 个字符转换成 word2 的前 j 个字符所需的最少操作数。

以下是解决这个问题的步骤：

1. 初始化一个 (m+1) x (n+1) 的二维数组 dp，其中 m 和 n 分别是 word1 和 word2 的长度。
  dp[i][0] 表示将 word1 的前 i 个字符转换为空字符串所需的最少操作数（即删除 i 次），
  dp[0][j] 表示将空字符串转换为 word2 的前 j 个字符所需的最少操作数（即插入 j 次）。

2. 遍历 word1 和 word2，更新二维数组 dp。对于每一对字符 word1[i] 和 word2[j]：
  如果 word1[i] == word2[j]，则不需要任何操作，因此 dp[i][j] = dp[i-1][j-1]。
  如果 word1[i] != word2[j]，我们可以进行插入、删除或替换操作。选择这三种操作中的最小操作数，并加一（代表当前操作）。
  
3. 最后，dp[m][n] 就是将 word1 转换成 word2 所需的最少操作数。
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # 初始化dp数组
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 初始化边界条件
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        # 动态规划计算所有dp值
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j],    # 删除操作
                                   dp[i][j - 1],    # 插入操作
                                   dp[i - 1][j - 1] # 替换操作
                                  ) + 1
        return dp[m][n]








