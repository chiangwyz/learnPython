"""
当最终找不到目标值时，left 和 right 指针会相互靠近，直至 left 超过 right。
此时，left 指针的位置就是目标值应该插入的位置。这是因为：
1. 如果目标值小于数组中的所有元素，那么在第一次比较时，它就会被判断为小于中间的元素，
    导致 right 指针移动到中间元素的左侧。最终，left 指针将指向数组的第一个位置（索引为0），这也是目标值应该插入的位置。
2. 如果目标值大于数组中的一些元素，但小于其他的元素，那么在比较过程中，left 和 right 指针会不断调整，直到 left 指向第一个大于目标值的元素的位置。
    此时，right 已经位于最后一个小于目标值的元素的位置，而 left 正好位于目标值应该插入的位置。
3. 如果目标值大于数组中的所有元素，那么 left 指针将不断向右移动，直到超出数组的末尾。
    在这种情况下，left 指针的位置（等于数组的长度）就是目标值应该插入的位置。
4. 总结来说，return left 语句返回的是目标值应该插入的位置，无论目标值是否存在于数组中。
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


# test
import unittest


class TestSearchInsert(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_target_in_list(self):
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 5), 2)

    def test_target_greater_than_all(self):
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 7), 4)

    def test_target_less_than_all(self):
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 0), 0)

    def test_target_between_elements(self):
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 2), 1)

    def test_empty_list(self):
        self.assertEqual(self.solution.searchInsert([], 5), 0)

    def test_single_element_list(self):
        self.assertEqual(self.solution.searchInsert([3], 2), 0)
        self.assertEqual(self.solution.searchInsert([3], 3), 0)
        self.assertEqual(self.solution.searchInsert([3], 4), 1)


if __name__ == '__main__':
    unittest.main()
