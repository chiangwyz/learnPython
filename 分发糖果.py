"""
n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。
你需要按照以下要求，给这些孩子分发糖果：
每个孩子至少分配到 1 个糖果。
相邻两个孩子评分更高的孩子会获得更多的糖果。
请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。
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



