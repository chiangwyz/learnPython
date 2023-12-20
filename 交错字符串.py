"""
要验证 s3 是否是由 s1 和 s2 交错组成，我们可以使用动态规划的方法。
动态规划是一种通过将问题分解成更小的子问题来解决复杂问题的方法。
在这个问题中，我们可以创建一个二维数组 dp，其中 dp[i][j] 表示 s1 的前 i 个字符和 s2 的前 j 个字符是否能交错组成 s3 的前 i+j 个字符。

我们可以按以下步骤进行：

1. 初始化 dp 数组。dp[0][0] 为 True，因为两个空字符串可以组成一个空字符串。
    接下来，我们初始化 dp 的第一行和第一列。dp[i][0] 为 True，如果 s1 的前 i 个字符和 s3 的前 i 个字符相同；
    同理，dp[0][j] 为 True，如果 s2 的前 j 个字符和 s3 的前 j 个字符相同。
    
2. 填充 dp 数组的剩余部分。对于每个 i 和 j，我们检查 s1[i-1] 是否等于 s3[i+j-1] 以及 s2[j-1] 是否等于 s3[i+j-1]。
    如果任一条件为真，并且相应的 dp[i-1][j] 或 dp[i][j-1] 也为真，那么 dp[i][j] 就为真。

3. 返回 dp 数组的最后一个元素 dp[len(s1)][len(s2)]，它表示整个 s1 和 s2 是否能交错组成整个 s3。
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 如果 s3 的长度不等于 s1 和 s2 长度之和，直接返回 False
        if len(s1) + len(s2) != len(s3):
            return False

        # 初始化 dp 数组
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        # 两个空字符串可以组成一个空字符串
        dp[0][0] = True  
        
        # 初始化 dp 的第一列
        for i in range(1, len(s1) + 1):
            if dp[i - 1][0] and s1[i - 1] == s3[i - 1]:
                dp[i][0] = True
            else:
                dp[i][0] = False

        """
        dp[0][j - 1] 是否为 True：这表示 s2 的前 j-1 个字符是否能单独交错组成 s3 的前 j-1 个字符。
        s2[j - 1] 是否等于 s3[j - 1]：这检查 s2 的第 j 个字符是否与 s3 的第 j 个字符相同。
        """
        # 初始化 dp 的第一行
        for j in range(1, len(s2) + 1):
            if dp[0][j - 1] and s2[j - 1] == s3[j - 1]:
                dp[0][j] = True
            else:
                dp[0][j] = False


        # 填充 dp 数组的其余部分
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                # 检查 s1[i-1] 或 s2[j-1] 是否与 s3[i+j-1] 相等
                # 并根据前一个状态更新 dp[i][j]
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                           (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])

        # 返回最后一个元素的值，表示是否能够交错组成
        return dp[len(s1)][len(s2)]















