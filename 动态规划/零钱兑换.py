"""
可以使用动态规划的方法。

1. 初始化动态规划数组：创建数组 dp，其长度为 amount + 1，用来存储每个金额所需的最少硬币数。
    初始时，除了 dp[0] 被设置为0（因为组成金额0不需要任何硬币）之外，
    其他所有元素都被设置为一个大于可能的最大硬币数量的值，这里我们使用 amount + 1。

2. 填充动态规划数组：对于每个金额 a（从1到 amount），我们尝试使用每种硬币 coin，如果 coin 的面额不超过 a，
    我们就计算使用这枚硬币后剩余金额（即 a - coin）所需的最少硬币数加上这枚硬币本身（即 1 + dp[a - coin]），
    并与当前存储的值比较，取较小的一个。

3. 检查并返回结果：最后，我们检查 dp[amount] 的值。
    如果它等于 amount + 1，这意味着没有办法组成这个金额，我们返回 -1。
    否则，我们返回 dp[amount]，它代表了组成金额所需的最少硬币数量。
"""
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # 创建一个数组，用于存储每个金额所需的最少硬币数
        dp = [amount + 1] * (amount + 1)
        
        # 基础情况：0金额需要0硬币
        dp[0] = 0
    
        # 遍历每个金额
        for a in range(1, amount + 1):
            # 尝试每种硬币
            for coin in coins:
                # 如果硬币面额不超过当前金额
                if coin <= a:
                    # 更新数组中的最少硬币数
                    dp[a] = min(dp[a], 1 + dp[a - coin])
    
        # 检查是否能组成金额，返回结果
        return dp[amount] if dp[amount] != amount + 1 else -1
