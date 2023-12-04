"""
通过随机选择一个基准数（pivot），然后将数组分为三部分：大于、等于和小于基准数的元素。
这种方法在处理包含重复元素的数组时特别有效，因为它将等于 pivot 的所有元素归为一类，
这样可以减少递归时的数组大小。
在这个实现中：
1. 如果第 k 大的元素在 big 数组中，递归地在 big 中寻找。
2. 如果第 k 大的元素不在 big 中，但在 small 数组中，根据 k 和 small 数组的大小递归地在 small 中寻找。
3. 如果第 k 大的元素不在 big 和 small 中，它必然在 equal 中，直接返回 pivot。

这个思路真的很简洁，也容易理解。
"""
import random

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        def quick_select(nums, k):
            # 随机选择基准数
            pivot = random.choice(nums)
            big, equal, small = [], [], []
            # 将大于、小于、等于 pivot 的元素划分至 big, small, equal 中
            for num in nums:
                if num > pivot:
                    big.append(num)
                elif num < pivot:
                    small.append(num)
                else:
                    equal.append(num)

            if len(big) >= k:
                # 第 k 大元素在 big 中，递归划分
                return quick_select(big, k)
                
            if len(big) + len(equal) < k:
                # 第 k 大元素在 small 中，递归划分
                return quickSelect(small, k - len(big) - len(equal))
                
            # 第 k 大元素在 equal 中，直接返回 pivot
            return pivot
        
        return quick_select(nums, k)
