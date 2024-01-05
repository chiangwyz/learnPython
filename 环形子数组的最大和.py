"""
关键在于处理数组的环形特性，这意味着数组的末尾和开头是相连的。为了解决这个问题，我们需要考虑两种情况：

1. 最大子数组和在数组的非环形部分。这个可以通过常规的最大子数组和算法（如Kadane算法）来解决。
2. 最大子数组和在数组的环形部分。这种情况可以通过计算整个数组的总和减去最小子数组和来处理。
  这里最小子数组也可以用类似Kadane算法的方式求得。
3. 最后，我们需要比较这两种情况的结果，取最大值。
  但是要注意一个特殊情况，即当数组中所有元素都是负数时，我们不能选择整个数组（这会使子数组为空），因此只能选择第一种情况。

其它知识。
数组取反操作 ([-x for x in nums]): 这个列表推导式的作用是将数组 nums 中的每个元素取反。
例如，如果 nums = [3, -2, 2, -3]，则这个操作后的数组将变为 [-3, 2, -2, 3]。

在一个环形数组中，从总和中减去最小子数组和来得到最大子数组和是一种巧妙的方法。
这种方法的有效性基于以下理解：

1. 环形数组的特点：在一个环形数组中，一个子数组可以是数组的一部分，也可以跨越数组的末尾和开头。
  因此，找到最大子数组和的关键在于考虑所有可能的子数组，包括那些跨越数组末尾和开头的子数组。

2. 两种情况：在环形数组中，有两种可能的情况可以得到最大子数组和：
  非环形部分的子数组：这是传统的最大子数组和问题，可以直接应用Kadane算法。
  包含环形部分的子数组：这种情况下，最大子数组实际上是数组的两端部分。为了找到这个子数组，我们可以反向思考：从整个数组中移除一个子数组，使得剩余部分的和最大。
3. 计算包含环形部分的最大子数组和：要找到包含环形部分的最大子数组和，我们需要从数组总和中减去一个最小的子数组和。
  这是因为当我们移除一个和最小的子数组时，剩余的部分（即包含环形部分的子数组）的和就会是最大的。

4. 实现方法：为了找到最小子数组和，我们可以将数组中的每个数取反，然后应用Kadane算法。这个算法会找到取反数组的最大子数组和，这实际上就是原始数组的最小子数组和。

综上所述，通过从总和中减去最小子数组和，我们可以得到包含环形部分的最大子数组和。
然后，我们将这个值与非环形部分的最大子数组和（直接用Kadane算法计算）进行比较，取二者中的较大值，这就是整个环形数组的最大子数组和。
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
