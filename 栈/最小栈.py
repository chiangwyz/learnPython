"""
使用两个栈：一个是主栈 self.stack，用于存储所有元素；
另一个是辅助栈 self.min_stack，用于跟踪当前栈中的最小元素。
可以在任何时候以 O(1) 的复杂度获取到最小值。
"""


class MinStack:
    def __init__(self):
        # 主栈，用于存储所有元素
        self.stack = list()
        # 辅助栈，用于存储每个状态下的最小值
        self.min_stack = list()

    def push(self, val: int) -> None:
        # 向栈中添加一个元素
        self.stack.append(val)
        # 如果辅助栈为空或者新元素小于等于辅助栈的栈顶元素，则将新元素也推入辅助栈
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # 从栈中移除顶部元素
        if not self.stack:
            raise IndexError("pop from an empty stack")
        top = self.stack.pop()

        # 如果主栈的顶部元素与辅助栈的顶部元素相等，则辅助栈也弹出顶部元素
        if self.min_stack and top == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        # 获取栈顶元素
        if not self.stack:
            raise IndexError("top from an empty stack")
        return self.stack[-1]

    def getMin(self) -> int:
        # 获取栈中的最小元素
        if not self.min_stack:
            raise IndexError("getMin from an empty stack")
        return self.min_stack[-1]


# test
def test_min_stack():
    # 创建 MinStack 实例
    min_stack = MinStack()

    # 测试空栈情况
    try:
        min_stack.pop()
        assert False, "pop from empty stack did not raise exception"
    except IndexError:
        pass

    try:
        min_stack.top()
        assert False, "top from empty stack did not raise exception"
    except IndexError:
        pass

    try:
        min_stack.getMin()
        assert False, "getMin from empty stack did not raise exception"
    except IndexError:
        pass

    # 测试单个元素
    min_stack.push(10)
    assert min_stack.top() == 10, "Top should be 10 after pushing 10"
    assert min_stack.getMin() == 10, "Min should be 10 after pushing 10"

    # 测试多个元素
    min_stack.push(20)
    assert min_stack.top() == 20, "Top should be 20 after pushing 20"
    assert min_stack.getMin() == 10, "Min should still be 10"

    min_stack.push(5)
    assert min_stack.top() == 5, "Top should be 5 after pushing 5"
    assert min_stack.getMin() == 5, "Min should be 5 after pushing 5"

    # 测试 pop 功能
    min_stack.pop()
    assert min_stack.top() == 20, "Top should be 20 after popping 5"
    assert min_stack.getMin() == 10, "Min should still be 10 after popping 5"

    print("All tests passed.")


# 运行测试
test_min_stack()
