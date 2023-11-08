"""
该问题挺有意思的，其核心点位将左右两边的最大值分开来更新
if height[left] >= left_max: 当当前值超过最大值时，才需要更新
"""
class Solution:
    def trap(self, height: list[int]) -> int:
        if height is None:
            return 0

        length = len(height)
        result = 0

        left = 0
        right = length - 1

        left_max = height[0]
        right_max = height[right]

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    result += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    result += right_max - height[right]
                right -= 1

        return result
      
