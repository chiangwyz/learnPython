"""
要颠倒给定的 32 位无符号整数的二进制位，我们可以遵循以下步骤：

1. 初始化结果：设置一个变量 res 为 0，它将存储最终反转后的结果。
2. 遍历32位：因为输入是一个 32 位的整数，我们需要遍历这 32 位。对于每一位：
    将 res 向左移动一位，为新的位腾出空间。
    从 n 中取出最后一位（n & 1），并将其加到 res 上。
    将 n 向右移动一位，移除已经处理过的最后一位。
3. 返回结果：遍历完成后，res 中存储的就是反转后的整数。

补充知识：
1. res = res << 1 这行代码执行一个左位移操作。
    << 是左位移操作符，res << 1 表示将 res 中的二进制位全部向左移动一位（最右边补 0）。
2. n = n >> 1 这行代码执行一个右位移操作。
    >> 是右位移操作符，n >> 1 表示将 n 中的二进制位全部向右移动一位（最左边补 0）。
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):  # 遍历32位
            res = res << 1  # 将res左移一位
            res += n & 1  # 将n的最后一位加到res上
            n = n >> 1  # 将n右移一位
        return res


# test
import unittest


class TestSolution(unittest.TestCase):
    def test_reverseBits(self):
        sol = Solution()
        # 测试用例 1
        self.assertEqual(sol.reverseBits(0b00000010100101000001111010011100), 964176192)
        # 测试用例 2
        self.assertEqual(sol.reverseBits(0b11111111111111111111111111111101), 3221225471)


if __name__ == '__main__':
    unittest.main()
