"""
在这个实现中，使用了两个栈：一个是主栈 self.stack，用于存储所有元素；
另一个是辅助栈 self.min_stack，用于跟踪当前栈中的最小元素。
这样可以在任何时候以 O(1) 的复杂度获取到最小值。
"""
class MinStack:
    def __init__(self):
        self.stack = list()       # 主栈，用于存储所有元素
        self.min_stack = list()   # 辅助栈，用于存储每个状态下的最小值

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

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(val)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
