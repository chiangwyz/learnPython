"""
示例：创建最小堆和最大堆
"""
import heapq

# 创建一个空的最小堆
min_heap = []
heapq.heapify(min_heap)

# 添加一些元素
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 4)
heapq.heappush(min_heap, -4)
heapq.heappush(min_heap, 40)
heapq.heappush(min_heap, -40)

# 弹出最小元素
min_element = heapq.heappop(min_heap)

print("min_element =", min_element)

# 创建最大堆，通过存储元素的相反数
max_heap = []
heapq.heapify(max_heap)

# 添加一些元素（存储它们的相反数）
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -4)
heapq.heappush(max_heap, -13)
heapq.heappush(max_heap, 34)
heapq.heappush(max_heap, 45)
heapq.heappush(max_heap, -33)

# 弹出最大元素（实际上是最小的相反数）
max_element = -heapq.heappop(max_heap)

print("max_element =", max_element)