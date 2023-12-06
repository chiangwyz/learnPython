"""
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。
请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例 2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：
输入：nums = [], target = 0
输出：[-1,-1]

这个问题的解决思路是使用两次二分查找。首先，我们需要定义两个辅助函数：binarySearchLeft 和 binarySearchRight。这两个函数分别用于找到目标值 target 在数组 nums 中的最左侧位置和最右侧位置。

binarySearchLeft 函数：
我们初始化两个指针 left 和 right 分别指向数组的起始位置和结束位置。
进行二分查找。如果中间位置的值小于 target，我们将 left 移动到 mid + 1；否则，将 right 移动到 mid - 1。
当 left 超过 right 时，二分查找结束。此时 left 指向的位置就是 target 的最左侧位置。

binarySearchRight 函数：
这个函数的逻辑类似于 binarySearchLeft，但是寻找的是 target 的最右侧位置。
当中间位置的值小于等于 target 时，我们移动 left 到 mid + 1；否则，移动 right 到 mid - 1。
当 left 超过 right 时，right 指向的位置就是 target 的最右侧位置。
最后，我们比较这两个位置。如果 left 指针小于等于 right 指针，说明 target 存在于数组中，我们返回这两个指针的位置作为结果；如果 left 指针大于 right 指针，说明 target 不存在于数组中，我们返回 [-1, -1]。

"""
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
      # 寻找目标值的最左侧位置
      def binarySearchLeft(nums, target):
          left, right = 0, len(nums) - 1
          while left <= right:
              mid = left + (right - left) // 2  # 计算中间位置
              if nums[mid] < target:            # 如果中间值小于目标值
                  left = mid + 1                # 移动左指针
              else:                             # 否则
                  right = mid - 1               # 移动右指针
          return left                           # 返回左指针，即最左侧位置
  
      # 寻找目标值的最右侧位置
      def binarySearchRight(nums, target):
          left, right = 0, len(nums) - 1
          while left <= right:
              mid = left + (right - left) // 2  # 计算中间位置
              if nums[mid] <= target:           # 如果中间值小于等于目标值
                  left = mid + 1                # 移动左指针
              else:                             # 否则
                  right = mid - 1               # 移动右指针
          return right                          # 返回右指针，即最右侧位置
  
      left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
      if left <= right:                         # 如果左指针小于等于右指针
          return [left, right]                  # 返回这两个指针的位置
      return [-1, -1]                           # 否则，表示目标值不在数组中，返回[-1, -1]

# 测试示例
example1 = [5,7,7,8,8,10]
target1 = 8

example2 = [5,7,7,8,8,10]
target2 = 6

example3 = []
target3 = 0

# 获取结果
result1 = searchRange(example1, target1)
result2 = searchRange(example2, target2)
result3 = searchRange(example3, target3)

result1, result2, result3


