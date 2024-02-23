"""
两个知识点：
1. 需要在循环中更新最低价格
2. 若没有更新价格，则每次检查是否超过最大利润
"""
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # 如果数组为空或只有一个价格数据，无法进行交易
        if len(prices) < 2:
            return 0

        # 初始化最小价格为第一天的价格
        min_price = prices[0]
        # 初始化最大利润为0
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                if price - min_price > max_profit:
                    max_profit = price - min_price

        return max_profit


