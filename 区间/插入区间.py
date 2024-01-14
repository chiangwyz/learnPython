"""
1. 初始化输出列表：创建一个空列表，用于存储最终的区间序列。
2. 添加所有在新区间之前结束的区间：遍历给定的区间列表，将所有在新区间开始之前结束的区间添加到输出列表中。
3. 合并重叠区间：接着处理与新区间重叠的区间。
   这可以通过不断更新新区间的起始和结束点来实现，直到遇到一个在新区间结束之后开始的区间。
4. 添加合并后的新区间：将更新后的新区间添加到输出列表。
5. 添加剩余的区间：最后，将所有在新区间之后开始的区间添加到输出列表。

这个算法首先处理所有不与新区间重叠的区间，然后合并所有重叠的区间，最后添加剩余的区间。
通过这种方式，算法保持了区间列表的排序和不重叠的特性。
"""


class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        merged = []
        i = 0
        n = len(intervals)

        # 添加所有在新区间之前结束的区间
        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1

        # 合并重叠区间
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1

        # 添加合并后的新区间
        merged.append(newInterval)

        # 添加剩余的区间
        while i < n:
            merged.append(intervals[i])
            i += 1

        return merged


# test
intervals1 = [[1, 3], [6, 9]]
newInterval1 = [2, 5]

intervals2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval2 = [4, 8]

sol = Solution()
print(sol.insert(intervals1, newInterval1))
print(sol.insert(intervals2, newInterval2))