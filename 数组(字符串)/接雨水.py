"""
该问题挺有意思的，题目关键点为将左右两边的最大值分开来更新
if height[left] >= left_max: 当当前值超过最大值时，才需要更新
"""
class Solution:
    def trap(self, height: list[int]) -> int:
        # 如果数组为空，返回雨水量为0
        if not height:
            return 0

        # 获取数组长度
        length = len(height)
        # 初始化结果变量为0
        result = 0

        # 初始化左右指针
        left = 0
        right = length - 1

        # 初始化左右最大高度
        left_max = height[0]
        right_max = height[right]

        # 当左指针小于右指针时，执行循环
        while left < right:
            # 如果左边的高度小于右边的高度
            if height[left] < height[right]:
                # 如果当前左边高度大于或等于左边最大高度，更新左边最大高度
                if height[left] >= left_max:
                    left_max = height[left]
                # 如果当前左边高度小于左边最大高度，计算雨水量并累加到结果变量中
                else:
                    result += left_max - height[left]
                # 左指针向右移动
                left += 1
            # 如果右边的高度小于或等于左边的高度
            else:
                # 如果当前右边高度大于或等于右边最大高度，更新右边最大高度
                if height[right] >= right_max:
                    right_max = height[right]
                # 如果当前右边高度小于右边最大高度，计算雨水量并累加到结果变量中
                else:
                    result += right_max - height[right]
                # 右指针向左移动
                right -= 1

        # 返回计算出的雨水总量
        return result


import unittest

class TestTrapFunction(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_empty_array(self):
        self.assertEqual(self.solution.trap([]), 0, "Should be 0 for empty array")

    def test_single_element_array(self):
        self.assertEqual(self.solution.trap([1]), 0, "Should be 0 for single element array")

    def test_no_trap(self):
        self.assertEqual(self.solution.trap([1, 2, 3, 4, 5]), 0, "Should be 0 for strictly increasing array")
        self.assertEqual(self.solution.trap([5, 4, 3, 2, 1]), 0, "Should be 0 for strictly decreasing array")

    def test_simple_trap(self):
        self.assertEqual(self.solution.trap([3, 0, 2]), 2, "Should trap 2 units of water")

    def test_complex_trap(self):
        self.assertEqual(self.solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6, "Should trap 6 units of water")
        self.assertEqual(self.solution.trap([4, 2, 0, 3, 2, 5]), 9, "Should trap 9 units of water")

if __name__ == '__main__':
    unittest.main()

