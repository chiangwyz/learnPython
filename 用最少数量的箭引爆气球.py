"""
为了找到引爆所有气球所需的最小弓箭数，我们可以使用贪心算法。
核心思想是尽可能让一支箭穿过多个气球。
为此，我们需要找到重叠的气球区间，然后在这些区间的重叠部分射箭。
具体步骤如下：

1. 排序：首先按每个气球的结束坐标对气球进行排序。
2. 初始化：设置一个变量 arrows 来记录所需的箭数，初始为 0。
   设置一个变量 end 来表示当前箭能够到达的最远位置，初始为负无穷大。
3. 遍历气球：遍历每个气球，如果当前气球的起始位置大于 end，说明这个气球不能被前一支箭射中，需要再射出一支新的箭，并更新 end 为当前气球的结束位置。
   如果当前气球的起始位置小于或等于 end，则可以不增加箭的数量，继续遍历下一个气球。
"""

class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        if not points:
            return 0

        # 根据每个气球的结束位置排序
        points.sort(key=lambda x: x[1])

        arrows = 1  # 至少需要一支箭
        end = points[0][1]  # 第一支箭能达到的最远位置

        for i in range(1, len(points)):
            # 如果当前气球的起始位置大于前一箭能达到的最远位置
            if points[i][0] > end:
                arrows += 1  # 需要再射出一支新的箭
                end = points[i][1]  # 更新能达到的最远位置

        return arrows


