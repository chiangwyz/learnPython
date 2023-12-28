"""
该解题最难的部分是从右到左遍历时，发放的糖果数组并不止直接+1，而是需要对比当前糖果与右边糖果加1后的大小。
"""

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        
        # 初始化糖果数组，每个孩子至少有一颗糖果
        candies = [1] * n
        
        # 从左到右遍历，确保评分高的孩子获得更多的糖果
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # 从右到左遍历，确保评分高的孩子获得更多的糖果
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        # 计算总糖果数
        return sum(candies)
