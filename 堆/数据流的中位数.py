"""
为了实现 MedianFinder 类，我们可以使用两个堆：一个最大堆来维护较小的一半元素，一个最小堆来维护较大的一半元素。
这种方法的关键在于保持两个堆的大小平衡（或者只差一个元素）。

1. 在 __init__ 方法中，初始化两个堆。最大堆用于存储较小的一半数字，最小堆用于存储较大的一半数字。

2. addNum 方法会将数字添加到相应的堆中。如果新数字小于最大堆的最大值，则添加到最大堆，否则添加到最小堆。添加之后，我们需要平衡两个堆的大小，确保两个堆的元素数量差不超过1。

3. findMedian 方法用于计算中位数。如果两个堆的大小相同，中位数是两个堆顶元素的平均值；如果大小不同，中位数是元素较多的那个堆的顶部元素。
"""

import heapq

class MedianFinder:

    def __init__(self):
        # 最大堆存储较小的一半元素，最小堆存储较大的一半元素
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # 如果num小于最大堆的最大值，则添加到最大堆
        if not self.max_heap or num < -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        
        # 平衡两个堆的大小
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        # 如果两个堆的大小相同，则中位数是两个堆顶元素的平均值
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        # 否则，中位数是元素较多的那个堆的顶部元素
        else:
            return -self.max_heap[0] if len(self.max_heap) > len(self.min_heap) else self.min_heap[0]

