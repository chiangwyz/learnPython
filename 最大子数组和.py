"""
使用动态规划算法，基本思想是遍历数组，同时维护两个变量：目前为止的最大子数组和和以及当前子数组和。
我们从数组的第一个元素开始，逐个考虑每个元素，并更新这两个变量。
如果当前子数组的和变为负数，我们就重置它为下一个元素，因为负数会减小子数组的和。
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 初始化最大子数组和为数组的第一个元素
        max_sum = nums[0]
        # 初始化当前子数组的和为0
        current_sum = 0

        # 遍历数组中的每个元素
        for num in nums:
            # 如果当前子数组和小于0，则丢弃当前子数组，并从当前元素重新开始计算
            if current_sum < 0:
                current_sum = num
            else:
                # 否则，将当前元素添加到当前子数组和中
                current_sum += num
            
            # 更新最大子数组和
            max_sum = max(max_sum, current_sum)

        return max_sum
