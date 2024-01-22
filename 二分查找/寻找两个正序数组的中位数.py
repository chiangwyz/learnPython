""""
我们可以采用一种分治方法来寻找两个已排序数组的中位数，达到时间复杂度为 O(log(min(m,n)))。

这种方法基于以下观点：中位数是将一个集合划分为两个长度相等的子集，其一个子集中的所有元素都不大于另一个子集的任何元素。
这里，我们将问题转化为寻找两个排序数组中的第 k 小的数，其中 k = (m+n)/2 (或k=((m+n)/2) + 1)取决于 m+n 是奇数还是偶数。

下面是该方法的具体步骤：

1. 首先，我们需要定义一个辅助函数，用于寻找两个排序数组中的第 k 小的数。
2. 在每一步，我们比较两个数组中的第 k/2 个元素（我们需要小心处理边界情况，即当一个数组的长度小于 k/2 时）。
  然后，我们可以排除掉较小的那个数组的前 k/2 个元素（因为我们知道这些元素不可能是第 k 小的数）。
3. 我们重复这个过程，直到我们找到第 k 小的数。如果某一步中一个数组为空，那么另一个数组的第 k 个元素就是我们要找的数。
4. 对于中位数的特殊情况，如果 m+n 是奇数，我们只需要找到第 ((m+n)/2) + 1 小的数；
  如果是偶数，我们需要找到第 ((m+n)/2) 和 ((m+n)/2) + 1 小的数，并计算它们的平均值。
"""


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    def findKthElement(arr1, arr2, k):
        """
        辅助函数，用于在两个排序数组 arr1 和 arr2 中找到第 k 小的元素。
        """
        # 如果其中一个数组为空，则第 k 小的元素必定在另一个数组中
        if not arr1:
            return arr2[k - 1]
        if not arr2:
            return arr1[k - 1]
        # 如果 k 为 1，则返回两个数组首元素的较小值
        if k == 1:
            return min(arr1[0], arr2[0])

        # 计算两个数组中可以比较的元素位置
        mid1 = min(len(arr1), k // 2)
        mid2 = min(len(arr2), k // 2)

        # 比较并排除其中一个数组的部分元素
        if arr1[mid1 - 1] <= arr2[mid2 - 1]:
            return findKthElement(arr1[mid1:], arr2, k - mid1)
        else:
            return findKthElement(arr1, arr2[mid2:], k - mid2)

    total_length = len(nums1) + len(nums2)
    # 判断数组总长度是奇数还是偶数，据此返回中位数
    if total_length % 2 == 1:
        return findKthElement(nums1, nums2, total_length // 2 + 1)
    else:
        return (findKthElement(nums1, nums2, total_length // 2) + findKthElement(nums1, nums2,
                                                                                 total_length // 2 + 1)) / 2


# 测试函数
test1 = findMedianSortedArrays([1, 3], [2])
test2 = findMedianSortedArrays([1, 2], [3, 4])
