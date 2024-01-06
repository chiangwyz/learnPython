"""
要解决这个问题，我们可以采用一个有效的方法来生成和排序数对。
首先，由于 nums1 和 nums2 都是非递减顺序排列的，我们可以从这两个数组的起始位置开始生成数对，并使用一个最小堆（小根堆）来保持数对的顺序。最小堆能够确保我们总是能够取出当前和最小的数对。

接下来，我们可以按照以下步骤操作：

1. 初始化一个最小堆。
2. 将 nums1 中的每个元素与 nums2 中的第一个元素的组合加入堆中。
3. 弹出堆顶元素，并将对应 nums1 元素的下一个与当前 nums2 元素的组合加入堆中。
4. 重复步骤 3，直到找到 k 对数对或堆为空。

补充知识：
(nums1[i] + nums2[0], i, 0) 生成的是一个单个的元组元素。这个元组包含三个部分：

1. nums1[i] + nums2[0]：这是两个数组元素的和，来自 nums1 中索引为 i 的元素和 nums2 中索引为 0 的元素。
2. i：这是 nums1 中元素的索引。
3. 0：这是 nums2 中元素的索引，初始时指向 nums2 的第一个元素。

"""

import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k == 0:
            return []

        min_heap = []
        # 由于两个数组都是非递减排序，所以初始可以将nums1中的每个元素和nums2的第一个元素的组合放入堆中。
        for i in range(min(k, len(nums1))):  # 只考虑k和nums1长度的较小者
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))

        result = []
        # 从堆中弹出k个最小组合
        while k > 0 and min_heap:
            _, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            k -= 1
            if j + 1 < len(nums2):  # 如果nums2还有元素，继续添加新组合
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return result
