"""
为了解决这个问题，我们可以使用动态规划。思路是自底向上地计算每一层的最小路径和，直到达到顶部。
这种方式可以避免重复计算，并且不需要额外的空间来存储中间结果。具体步骤如下：

1. 从三角形的倒数第二层开始，对于每一层的每一个元素，计算通过这个元素到达底层的最小路径和。
  这个最小路径和等于当前元素的值加上它下一层的两个相邻元素的最小路径和。

2. 重复上述步骤，直到计算到三角形的顶部。

3. 三角形顶部的元素值就是最小路径和。
"""

class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)
        # 从三角形的倒数第二层开始向上计算
        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                # 更新当前位置的最小路径和
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]


import unittest

class TestSolution(unittest.TestCase):
    def test_minimumTotal(self):
        sol = Solution()
        self.assertEqual(sol.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]), 11)
        self.assertEqual(sol.minimumTotal([[-10]]), -10)


if __name__ == "__main__":
    test_solution = TestSolution()
    test_solution.test_minimumTotal()


