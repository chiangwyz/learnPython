"""
可以使用动态规划的方法。
动态规划的基本思想是将问题分解成更小的子问题，并使用这些子问题的解来构建原问题的解。

在这个特定的问题中，我们可以定义一个数组 dp，其中 dp[i] 表示组成金额 i 所需的最少硬币数量。
我们初始化 dp 数组中的每个元素为一个大数（比如 amount + 1），
表示最初我们无法用给定的硬币组成这些金额。显然，dp[0] 应该初始化为 0，因为组成金额 0 不需要任何硬币。

对于每个金额 i，我们遍历所有的硬币面额 coin，
并更新 dp[i] 为所有 dp[i - coin] + 1 中的最小值（这里 i - coin 表示使用了一枚面额为 coin 的硬币后剩下的金额）。
如果最终 dp[amount] 的值仍然是初始化的大数，这意味着我们无法组成该金额，因此返回 -1。否则，dp[amount] 就是所求的最少硬币数量。

在这段代码中，我们首先初始化一个长度为 amount + 1 的数组 dp，
所有元素都设置为 amount + 1。然后，对于每个金额从 1 到 amount，
我们尝试使用所有可能的硬币面额去更新 dp[i]。最终，我们根据 dp[amount] 是否还是初始值来判断是否可以组成该金额。
"""
def coinChange(coins, amount):
    # 初始化dp数组，初始值设为一个大数
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    # 遍历每个金额，尝试使用所有硬币
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # 如果dp[amount]还是初始值，表示无法组成该金额
    return dp[amount] if dp[amount] != amount + 1 else -1
