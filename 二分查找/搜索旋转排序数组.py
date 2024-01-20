"""
这个问题可以通过二分查找算法来解决，以满足时间复杂度为 O(log n) 的要求。
由于数组是在某个未知下标处旋转的，我们需要在常规的二分查找中加入额外的逻辑来处理这种旋转。

1. 初始化左边界 left 为 0，右边界 right 为 nums.length - 1。
2. 进行二分查找。当 left 小于等于 right 时，计算中间位置 mid。
3. 检查 nums[mid] 是否等于 target。如果是，返回 mid。
4. 确定旋转的部分。如果 nums[left] 小于等于 nums[mid]，则左半部分是有序的；否则，右半部分是有序的。
5. 根据有序部分来决定如何移动边界。如果 target 在有序部分的范围内，移动对应边界来缩小查找范围；
    否则，移动另一边的边界。
6. 如果找不到 target，返回 -1。
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # 如果中间的数就是目标值，直接返回下标
            if nums[mid] == target:
                return mid

            # 判断左侧是否是有序的
            if nums[left] <= nums[mid]:
                # 如果目标值在左侧的有序部分中，移动右边界
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    # 否则，移动左边界
                    left = mid + 1
            else:
                # 右侧是有序的
                # 如果目标值在右侧的有序部分中，移动左边界
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    # 否则，移动右边界
                    right = mid - 1

        # 找不到目标值，返回 -1
        return -1


# test
import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        self.assertEqual(self.solution.search(nums, target), 4)

    def test_example2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        self.assertEqual(self.solution.search(nums, target), -1)

    def test_example3(self):
        nums = [1]
        target = 0
        self.assertEqual(self.solution.search(nums, target), -1)

    def test_sorted_array(self):
        nums = [1, 2, 3, 4, 5, 6]
        target = 4
        self.assertEqual(self.solution.search(nums, target), 3)

    def test_single_element(self):
        nums = [1]
        target = 1
        self.assertEqual(self.solution.search(nums, target), 0)

    def test_large_array(self):
        nums = list(range(1000))
        target = 500
        self.assertEqual(self.solution.search(nums, target), 500)


# 运行测试
if __name__ == '__main__':
    unittest.main()
