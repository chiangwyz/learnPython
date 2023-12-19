"""
可以通过动态规划来解决。我们需要找到两次买卖股票的最大利润，但在第二次购买之前必须卖掉之前的股票。

这里的关键是维护四个变量，分别代表以下四种状态：
1. 第一次买入股票后的最大利润。
2. 第一次卖出股票后的最大利润。
3. 第二次买入股票后的最大利润（包含第一次的利润）。
4. 第二次卖出股票后的最大利润（最终结果）。

我们遍历价格数组，对于每一天的价格，我们更新以上四个变量。
初始状态下，第一次买入的利润是负的，因为我们支付了购买股票的费用，而其他三个利润都是0。
遍历过程中，我们不断更新这四个变量以反映到当前为止的最佳决策。
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        # 初始化四个变量
        # first_buy：第一次买入股票后的最大利润
        # first_sell：第一次卖出股票后的最大利润
        # second_buy：第二次买入股票后的最大利润
        # second_sell：第二次卖出股票后的最大利润
        first_buy, first_sell, second_buy, second_sell = -float('inf'), 0, -float('inf'), 0

        for price in prices:
            # 更新第一次买入和第一次卖出后的最大利润
            first_buy = max(first_buy, -price)  # 第一次买入股票的最大利润，可能是之前买的，或者今天买的
            first_sell = max(first_sell, first_buy + price)  # 第一次卖出股票的最大利润

            # 更新第二次买入和第二次卖出后的最大利润
            second_buy = max(second_buy, first_sell - price)  # 第二次买入股票的最大利润，考虑到第一次的利润
            second_sell = max(second_sell, second_buy + price)  # 第二次卖出股票的最大利润

        return second_sell  # 最终结果

