"""
合并k个有序数组为一个有序数组。
"""

# 方法一

import heapq


class Solution:
    def merge_k_sorted_arrays(self, arrays: list[list[int]]):
        # 创建一个最小堆
        min_heap = []
        # 初始化堆，将每个数组的第一个元素及其索引和数组索引放入堆中
        for i, array in enumerate(arrays):
            if array:
                # 注入最小堆的元组内元素依次为：数组的第一个元素，数组索引，元素索引
                heapq.heappush(min_heap, (array[0], i, 0))

        result = []
        # 当堆不为空时，继续处理
        while min_heap:
            # 弹出最小元素
            val, arr_idx, ele_idx = heapq.heappop(min_heap)
            result.append(val)
            # 如果该数组还有元素，将下一个元素加入堆中
            if ele_idx + 1 < len(arrays[arr_idx]):
                heapq.heappush(min_heap, (arrays[arr_idx][ele_idx + 1], arr_idx, ele_idx + 1))

        return result


# test
solution = Solution()

# 示例输入
arrays = [[1, 4, 5], [1, 3, 4], [2, 6]]

print(solution.merge_k_sorted_arrays(arrays))
