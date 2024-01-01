class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 初始化左右指针
        left, right = 0, len(nums) - 1

        # 当左指针小于右指针时循环
        while left < right:
            # 计算中间位置
            mid = (left + right) // 2

            # 比较中间元素和其右侧元素
            if nums[mid] > nums[mid + 1]:
                # 如果中间元素大于其右侧元素，则峰值在左半边，调整右指针
                right = mid
            else:
                # 否则，峰值在右半边，调整左指针
                left = mid + 1

        # 返回峰值元素的索引
        return left

