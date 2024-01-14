"""
lambda x: x[0] 这个表达式可以解读为：

在代码 intervals.sort(key=lambda x: x[0]) 中，这个 lambda 函数作为 sort 方法的 key 参数。
这个 lambda 函数接收 intervals 列表中的每个元素（即一个区间，比如 [start, end]），并返回这个区间的第一个元素（即 start）。
sort 方法使用这个返回值（start）来决定列表中元素的排序顺序。

lambda 是一个关键字，用于定义匿名函数。
x 是这个匿名函数的参数。在这个上下文中，x 代表 intervals 列表中的一个元素，每个元素都是一个区间，如 [start, end]。
冒号 : 用于分隔参数和函数体。
x[0] 是函数体部分，表示返回 x 这个区间的第一个元素，也就是区间的起始值 start。
所以，lambda x: x[0] 表示一个函数，这个函数接受一个参数 x（在这里是一个区间），并返回这个区间的起始值。
在 sort 方法中使用这个函数作为 key 参数，告诉 sort 按照区间的起始值来对区间进行排序。
"""

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # 按区间的起始位置进行排序
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # 如果合并列表为空，或者当前区间的起始位置大于合并列表中最后区间的结束位置
            # 则不重叠，直接添加到合并列表中
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则，有重叠，合并当前区间和合并列表中的最后一个区间
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


# test
intervals = [[1,3],[2,6],[8,10],[15,18]]

sol = Solution()
print(sol.merge(intervals))
