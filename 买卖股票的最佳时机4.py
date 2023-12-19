"""
这个问题可以通过动态规划来解决。动态规划是一种用来解决复杂问题的方法，通过将问题分解为更简单的子问题来解决。

为了解决这个问题，我们可以使用一个二维数组 dp 来存储中间结果。
数组 dp[i][j] 表示在第 i 天，最多进行 j 笔交易所能获得的最大利润。
这里，i 范围是从 0 到 len(prices)-1（即股票价格数组的长度），而 j 的范围是从 0 到 k。

算法的基本思想是：对于每一天 i 和每一笔交易 j，我们可以选择不进行交易，或者是在之前某一天买入股票后在第 i 天卖出。因此，状态转移方程可以写成：
dp[i][j]=max(dp[i−1][j],max_{x<i}(dp[x][j−1]+prices[i]−prices[x]))

其中 dp[i-1][j] 表示在第 i 天不进行交易，而 dp[x][j-1] + prices[i] - prices[x] 表示在第 x 天买入，在第 i 天卖出。
"""

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # 如果价格列表为空，则无法进行交易，因此返回0
        if not prices:
            return 0

        n = len(prices)
        # 如果可进行的交易次数大于等于天数的一半，实际上没有交易次数的限制
        # 在这种情况下，可以使用贪心算法来求解，即只要后一天的价格比前一天高，就进行交易
        if k >= n // 2:
            # 初始化总利润为0
            total_profit = 0
            # 遍历每一天（从第二天开始）
            for i in range(1, n):
                # 计算当天价格与前一天价格的差值
                price_diff = prices[i] - prices[i - 1]
                # 如果价格上涨，则将差值加到总利润中
                if price_diff > 0:
                    total_profit += price_diff
            # 返回总利润
            return total_profit

        # 初始化动态规划表，dp[i][j] 表示在第i天最多进行j次交易所能获得的最大利润
        dp = [[0] * (k + 1) for _ in range(n)]

        # 遍历每一次交易
        for j in range(1, k + 1):
            # 初始化max_diff为第一天买入股票的负收益
            max_diff = -prices[0]
            # 遍历每一天
            for i in range(1, n):
                # 计算在第i天卖出股票的最大利润
                dp[i][j] = max(dp[i - 1][j], prices[i] + max_diff)
                # 更新max_diff，为之后的计算准备
                max_diff = max(max_diff, dp[i][j - 1] - prices[i])

        # 返回最后一天进行最多k次交易所能获得的最大利润
        return dp[n - 1][k]
