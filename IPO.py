"""
创建并维护最小堆 minCapitalHeap 时，堆是根据元组中的第一个元素，即 capital[i]，来进行排序的。
这是因为 Python 的 heapq 模块默认将元组的第一个元素作为排序的关键字。

在这个特定的场景中：

每个元素都是一个形如 (capital[i], profits[i]) 的元组。
heapq 将这些元组按照它们的 capital[i] 值（即启动项目所需的资本）进行排序。
最小堆保证了堆顶（即 minCapitalHeap[0]）总是所需资本最小的项目。
这个排序方式是自动的，基于 Python 元组比较的规则：首先比较元组的第一个元素，如果相同，则比较第二个元素，依此类推。
由于在这种情况下，我们只关心每个项目的启动资本，因此元组的第一个元素（capital[i]）成为排序的主要依据。
"""

import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # 初始化两个堆
        minCapitalHeap = []
        maxProfitHeap = []

        # 将所有项目加入到最小堆 minCapitalHeap
        for i in range(len(profits)):
            heapq.heappush(minCapitalHeap, (capital[i], profits[i]))

        # 进行 k 次投资
        for _ in range(k):
            # 将所有当前资本 w 能启动的项目加入到最大堆 maxProfitHeap
            while minCapitalHeap and minCapitalHeap[0][0] <= w:
                capital, profit = heapq.heappop(minCapitalHeap)
                heapq.heappush(maxProfitHeap, -profit)

            # 如果没有可投资的项目，就结束循环
            if not maxProfitHeap:
                break

            # 选择利润最大的项目进行投资，并更新资本
            w -= heapq.heappop(maxProfitHeap)

        return w


