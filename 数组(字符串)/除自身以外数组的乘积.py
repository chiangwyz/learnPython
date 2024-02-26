"""
该题目非常有趣，有几个细节需要注意，
1. 初始化应该为[0]
2. 计算右乘积，range的范围和数组的下标。
"""
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # 数组长度
        length = len(nums)

        if length == 0:
            return []

        # 初始化左乘积、右乘积和结果数组
        left = [0]*length
        right = [0] * length
        answer = [0] * length

        # 计算左乘积
        # 第一个元素左边没有其他元素，所以乘积为1
        left[0] = 1
        for i in range(1, length):
            left[i] = left[i-1] * nums[i-1]

        # 计算右乘积
        # 最后一个元素右边没有其他元素，所以乘积为1
        right[length-1] = 1
        for i in range(length-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        # 计算最终结果
        for i in range(length):
            answer[i] = left[i] * right[i]

        return answer


import unittest
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example(self):
        self.assertEqual(self.solution.productExceptSelf([1,2,3,4]), [24,12,8,6])

    def test_zero(self):
        self.assertEqual(self.solution.productExceptSelf([0,1]), [1,0])

    def test_negative(self):
        self.assertEqual(self.solution.productExceptSelf([-1,2,-3,4]), [-24,12,-8,6])

    def test_single_element(self):
        self.assertEqual(self.solution.productExceptSelf([42]), [1])

    def test_empty(self):
        self.assertEqual(self.solution.productExceptSelf([]), [])


if __name__ == "__main__":
    unittest.main()