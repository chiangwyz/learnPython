"""
这种解法非常巧妙，所以记录下来，从后往前合并，而且考虑了m=0或者n=0的情况
"""
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 从后向前合并，先填充nums1的后半部分
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1

        # 如果nums2还有剩余，直接复制到nums1的前面，nums1剩余的部分不需要操作，因为它们已经在正确的位置
        nums1[:n] = nums2[:n]


"""
单元测试
"""

import unittest

class TestMergeFunction(unittest.TestCase):
    def test_examples(self):
        solution = Solution()
        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3
        solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1,2,2,3,5,6])

        nums1 = [4,5,6,0,0,0]
        m = 3
        nums2 = [1,2,3]
        n = 3
        solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1,2,3,4,5,6])

        nums1 = [1,0]
        m = 1
        nums2 = [2]
        n = 1
        solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1,2])

        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1])

        nums1 = [2,0]
        m = 1
        nums2 = [1]
        n = 1
        solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1,2])


if __name__ == '__main__':
    unittest.main()

