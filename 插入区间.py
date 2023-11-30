"""
给你一个 无重叠的 ，按照区间起始端点排序的区间列表。
在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

示例 1：
输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]

示例 2：
输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。

示例 3：
输入：intervals = [], newInterval = [5,7]
输出：[[5,7]]

示例 4：
输入：intervals = [[1,5]], newInterval = [2,3]
输出：[[1,5]]

示例 5：
输入：intervals = [[1,5]], newInterval = [2,7]
输出：[[1,7]]

1. 初始化输出列表：创建一个空列表，用于存储最终的区间序列。
2. 添加所有在新区间之前结束的区间：遍历给定的区间列表，将所有在新区间开始之前结束的区间添加到输出列表中。
3. 合并重叠区间：接着处理与新区间重叠的区间。这可以通过不断更新新区间的起始和结束点来实现，直到遇到一个在新区间结束之后开始的区间。
4. 添加合并后的新区间：将更新后的新区间添加到输出列表。
5. 添加剩余的区间：最后，将所有在新区间之后开始的区间添加到输出列表。

"""


class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        merged = []
        i, n = 0, len(intervals)

        # 添加所有在新区间之前结束的区间
        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1

        # 合并重叠区间
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # 添加合并后的新区间
        merged.append(newInterval)

        # 添加剩余的区间
        while i < n:
            merged.append(intervals[i])
            i += 1

        return merged









