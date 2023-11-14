"""
爬楼梯这个题目很简单，也很经典了。斐波那契额数列，动态规划求解，但是偶然间发现这样的解法。简单易懂，时间复杂度还是O(1)，增加的只是空间复杂度。
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        a = 1
        b = 2
        c = 0
        for i in range(3, n + 1):
            c = a + b
            a = b
            b = c
        
        return c

        return b
