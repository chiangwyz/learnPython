class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
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


import unittest


class TestFindPeakElement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_element(self):
        self.assertEqual(self.solution.findPeakElement([1]), 0)

    def test_two_elements(self):
        self.assertEqual(self.solution.findPeakElement([1, 2]), 1)
        self.assertEqual(self.solution.findPeakElement([2, 1]), 0)

    def test_multiple_elements(self):
        self.assertIn(self.solution.findPeakElement([1, 2, 3, 1]), [2])
        self.assertIn(self.solution.findPeakElement([1, 3, 2, 1]), [1])

    def test_multiple_index(self):
        result = self.solution.findPeakElement([1, 2, 1, 3, 5, 6, 4])
        self.assertIn(result, [1, 5])

    def test_large_input(self):
        nums = list(range(1000)) + [1001] + list(range(999, 0, -1))
        self.assertEqual(self.solution.findPeakElement(nums), 1000)


if __name__ == '__main__':
    unittest.main()
