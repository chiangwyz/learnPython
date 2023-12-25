"""
由于题目允许我们在同一天卖出后立即再次买入，我们可以连续捕捉每次价格上涨的机会。
无论价格变动如何，只要有价格上涨，我们都可以通过买入和卖出来累积利润。
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit
