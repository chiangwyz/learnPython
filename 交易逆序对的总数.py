"""
要解决这个问题，我们可以使用一种名为“归并排序”的算法变体。
归并排序是一种分而治之的算法，它将数组分成两半，分别排序，然后合并。
在合并的过程中，我们可以计算逆序对的数量。

基本思路是这样的：当我们合并两个已排序的子数组时，如果从左边的数组中取出的元素大于从右边数组中取出的元素，
那么左边数组中当前元素及其后面的所有元素都会与这个右边的元素形成逆序对，因为左边的数组是已经排序的。

这个算法的时间复杂度是 O(n log n)，其中 n 是数组的长度。这是因为归并排序的时间复杂度是 O(n log n)，而我们在合并过程中计算逆序对的时间复杂度是 O(n)。
"""

from typing import List

class Solution:
    def reversePairs(self, record: List[int]) -> int:
        # 用于辅助合并排序的临时数组
        temp = [0] * len(record)
        return self.mergeSort(record, temp, 0, len(record) - 1)

    def mergeSort(self, record: List[int], temp: List[int], left: int, right: int) -> int:
        # 如果左边界大于等于右边界，则不需要排序
        if left >= right:
            return 0

        # 计算中间位置
        mid = (left + right) // 2
        # 递归地对左半部分和右半部分进行归并排序，并计算逆序对数量
        count = self.mergeSort(record, temp, left, mid) + \
                self.mergeSort(record, temp, mid + 1, right)
        
        # 合并两个已排序的子数组并计算逆序对
        count += self.merge(record, temp, left, mid, right)
        return count

    def merge(self, record: List[int], temp: List[int], left: int, mid: int, right: int) -> int:
        # 初始化指针和逆序对计数器
        i, j, k, count = left, mid + 1, left, 0

        # 合并两个子数组
        while i <= mid and j <= right:
            if record[i] <= record[j]:
                temp[k] = record[i]
                i += 1
            else:
                # 发现逆序对
                temp[k] = record[j]
                count += mid - i + 1
                j += 1
            k += 1

        # 将剩余元素复制到临时数组
        while i <= mid:
            temp[k] = record[i]
            i += 1
            k += 1
        while j <= right:
            temp[k] = record[j]
            j += 1
            k += 1

        # 将排序后的临时数组复制回原数组
        for i in range(left, right + 1):
            record[i] = temp[i]

        return count
