"""
问题：给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。

要实现一个基本的计算器来计算这类包含加号、减号、括号的数学表达式，你可以使用一个栈来辅助计算。
栈可以帮助我们处理括号内的表达式，并且管理不同级别的运算优先级。下面是具体的算法步骤：

1. 初始化一个栈stack来存储表达式中的数字和符号。
2. 遍历字符串 s 中的每个字符：
    如果是数字，需要继续向后查找，直到非数字字符，将整个数字作为一个整体处理。
    如果遇到加号（+）或减号（-），将前一个数字（如果有）和符号一起压入栈中。
    如果遇到左括号（(），将其作为分界符压入栈中。
    如果遇到右括号（)），则弹出栈中的元素进行计算，直到遇到左括号为止，计算结果再压入栈中。
3. 遍历完字符串后，如果栈中还有未处理的数字和运算符，需要继续进行计算。
4. 最终栈顶元素就是整个表达式的计算结果。
"""
import unittest


class Solution:
    def calculate(self, s: str) -> int:
        # 用于存储括号前的计算结果和符号
        stack = []
        # 当前读取的数字
        current_num = 0
        # 当前的符号，1 表示加，-1 表示减
        sign = 1
        # 当前的计算结果
        result = 0

        for ch in s:
            if ch.isdigit():
                # 如果字符是数字，将其添加到当前数字的末尾
                current_num = (current_num * 10) + int(ch)
            elif ch == '+':
                # 如果遇到加号，将之前的数字和符号加到结果中
                result += sign * current_num
                # 设置符号为加号
                sign = 1
                # 重置当前数字
                current_num = 0
            elif ch == '-':
                # 如果遇到减号，同样将之前的数字和符号加到结果中
                result += sign * current_num
                # 设置符号为减号
                sign = -1
                # 重置当前数字
                current_num = 0
            elif ch == '(':
                # 如果遇到左括号，将当前结果和符号压入栈中
                stack.append(result)
                stack.append(sign)
                # 重置符号和结果，准备计算括号内的表达式
                sign = 1
                result = 0
            elif ch == ')':
                # 如果遇到右括号，首先处理括号内最后的数字
                result += sign * current_num
                # 然后将结果乘以括号前的符号，并加上括号前的结果
                result *= stack.pop()  # 弹出括号前的符号
                result += stack.pop()  # 弹出括号前的累计结果
                current_num = 0  # 重置当前数字

        # 返回最终结果
        return result + sign * current_num


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_simple_expression(self):
        self.assertEqual(self.solution.calculate("1 + 1"), 2)

    def test_subtraction(self):
        self.assertEqual(self.solution.calculate("2 - 1 + 2"), 3)

    def test_expression_with_parentheses(self):
        self.assertEqual(self.solution.calculate("(1+(4+5+2)-3)+(6+8)"), 23)

    def test_expression_with_negative_numbers(self):
        self.assertEqual(self.solution.calculate("- (3 + (2 - 1))"), -4)

    def test_expression_with_spaces(self):
        self.assertEqual(self.solution.calculate(" 2-1 + 2 "), 3)

    def test_complex_expression(self):
        self.assertEqual(self.solution.calculate("2-(5-6)"), 3)


if __name__ == '__main__':
    unittest.main()
