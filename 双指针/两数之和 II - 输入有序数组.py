"""
使用了双指针策略来找出两个数的和等于给定目标数的元素下标。由于数组是按非递减顺序排列的，这种方法可以有效地在常量空间和线性时间内找到解。

注意，下标是从1开始的。
"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # 使用双指针，分别指向数组的开始和结束
        left = 0
        right = len(numbers) - 1  

        # 当左指针小于右指针时循环
        while left < right:  
            current_sum = numbers[left] + numbers[right]
            # 如果两数之和等于目标值，返回它们的下标
            if current_sum == target:  
                return [left + 1, right + 1]
            # 如果两数之和小于目标值，移动左指针
            elif current_sum < target:  
                left += 1
            # 如果两数之和大于目标值，移动右指针
            else:  
                right -= 1

        # 如果没有找到，返回空数组
        return []  

# 示例测试
sol = Solution()
print(sol.twoSum([2,7,11,15], 9))  # 输出：[1, 2]
print(sol.twoSum([2,3,4], 6))  # 输出：[1, 3]
print(sol.twoSum([-1,0], -1))  # 输出：[1, 2]

