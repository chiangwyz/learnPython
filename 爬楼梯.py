"""
爬楼梯这个题目很简单，也很经典。斐波那契额数列，使用动态规划求解。
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        # 初始化dp数组
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        
        # 动态规划填充dp数组
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]

# 创建Solution实例
sol = Solution()

# 测试案例
n1 = 2
n2 = 56
result1 = sol.climbStairs(n1)
result2 = sol.climbStairs(n2)


