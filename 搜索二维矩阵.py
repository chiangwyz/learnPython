"""
要解决这个问题，我们可以利用矩阵的两个特性来高效地查找目标值 target。
首先，因为每行的整数是非严格递增的，我们可以在每行内使用二分查找来快速确定目标值是否存在。
其次，由于每行的第一个整数大于前一行的最后一个整数，我们知道目标值只可能存在于一个行内。

因此，我们的算法可以分为两个步骤：

确定目标值可能所在的行。
在这一行内使用二分查找来查找目标值。
具体实现步骤如下：

遍历矩阵的每一行，比较每行的第一个元素和最后一个元素与目标值。如果目标值在这个范围内，就在这一行内进行二分查找。
在二分查找中，我们将行视为一个有序数组。设置两个指针，一个指向行的开始，另一个指向行的结束。
然后不断地将目标值与行中间元素进行比较，根据比较的结果调整指针，直到找到目标值或者搜索区间为空。
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 遍历每一行
        for row in matrix:
            # 如果目标值在当前行的范围内
            if target >= row[0] and target <= row[-1]:
                # 使用二分查找在当前行中查找目标值
                left, right = 0, len(row) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if row[mid] == target:
                        return True  # 找到目标值
                    elif row[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                return False  # 当前行没有找到目标值
        return False  # 没有任何一行包含目标值

