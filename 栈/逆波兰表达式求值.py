"""
要计算基于逆波兰表示法（后缀表达式）的算术表达式，我们可以使用一个栈来处理。
逆波兰表示法的一个关键特点是，操作符位于其操作数之后。下面是解决这个问题的算法：

1. 初始化一个空栈。
2. 遍历字符串数组 tokens。
3. 对于每个元素：
   如果它是一个操作数（数字），则将其推入栈中。
   如果它是一个操作符（'+'、'-'、'*' 或 '/'），则从栈中弹出两个顶部元素（注意：后弹出的是左操作数，先弹出的是右操作数），
   对它们执行相应的运算，并将结果推回栈中。
4. 在数组的最后，栈顶元素就是整个表达式的结果。
"""


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        # 初始化栈
        stack = []

        # 遍历每个元素
        for token in tokens:
            # 如果元素是运算符
            if token in "+-*/":
                # 从栈中弹出两个元素
                right = stack.pop()  # 右操作数
                left = stack.pop()  # 左操作数

                # 根据运算符进行运算
                if token == '+':
                    stack.append(left + right)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                else:  # 处理除法，注意 Python 中的整数除法需要向零截断
                    stack.append(int(left / right))
            else:
                # 如果元素是数字，则直接推入栈中
                stack.append(int(token))

        # 返回栈顶元素，即最终结果
        return stack.pop()


# 测试
test_cases = [
    ["2", "3", "+"],
    ["4", "13", "5", "/", "+"],
    ["10", "6", "9", "3", "+", "-11", "*", "/", "*"],
    ["2", "1", "+", "3", "*"],
    ["4", "13", "5", "/", "-"]
]


solution = Solution()

# 对每个测试用例进行求值
for case in test_cases:
    result = solution.evalRPN(case)
    print("表达式 {} 的结果为：{}".format(case, result))
