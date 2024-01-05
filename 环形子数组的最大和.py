"""
关键在于处理数组的环形特性，这意味着数组的末尾和开头是相连的。为了解决这个问题，我们需要考虑两种情况：

1. 最大子数组和在数组的非环形部分。这个可以通过常规的最大子数组和算法（如Kadane算法）来解决。
2. 最大子数组和在数组的环形部分。这种情况可以通过计算整个数组的总和减去最小子数组和来处理。
  这里最小子数组也可以用类似Kadane算法的方式求得。
3. 最后，我们需要比较这两种情况的结果，取最大值。
  但是要注意一个特殊情况，即当数组中所有元素都是负数时，我们不能选择整个数组（这会使子数组为空），因此只能选择第一种情况。
"""

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(nums: List[int]) -> int:
            """
            Kadane算法，用于计算最大子数组和
            """
            max_ending_here = max_so_far = nums[0]
            for x in nums[1:]:
                max_ending_here = max(x, max_ending_here + x)
                max_so_far = max(max_so_far, max_ending_here)
            return max_so_far

        # 情况1: 最大子数组和在非环形部分
        max_normal = kadane(nums)
        
        # 情况2: 最大子数组和在环形部分
        # 计算数组总和
        total_sum = sum(nums)
        # 计算最小子数组和
        min_subarray_sum = kadane([-x for x in nums])
        max_circular = total_sum + min_subarray_sum  # 加回因为取反而减掉的总和

        # 如果所有数字都是负数，max_circular将是0，这是不合理的。因此在这种情况下不考虑max_circular。
        if max_circular == 0:
            return max_normal

        return max(max_normal, max_circular)
