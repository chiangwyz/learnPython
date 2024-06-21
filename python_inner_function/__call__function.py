"""
__call__方法使类的实例像函数一样被调用。
它可以用于创建行为像函数的对象、实现装饰器、以及保持状态信息。
在你的代码中，它用于实现自定义比较器，使你能够根据特定的规则比较两个标签对象。

__call__方法确实是一个特殊的方法，目的是让一个类的实例能够像函数一样被调用。
虽然__call__方法的定义只能有一个，但在这个方法内部，你可以根据不同的条件执行不同的行为。
也就是说，__call__方法可以根据传入的参数或其他条件来决定执行什么行为。
"""

class MultiBehavior:
    def __init__(self):
        self.state = "initial"

    def __call__(self, action, *args):
        if action == "increment":
            return self.increment(*args)
        elif action == "decrement":
            return self.decrement(*args)
        elif action == "set_state":
            return self.set_state(*args)
        else:
            raise ValueError(f"Unknown action: {action}")

    def increment(self, value):
        return value + 1

    def decrement(self, value):
        return value - 1

    def set_state(self, state):
        self.state = state
        return f"State set to {state}"


# 创建 MultiBehavior 的实例
mb = MultiBehavior()

# 执行不同的行为
print(mb("increment", 5))   # 输出 6
print(mb("decrement", 5))   # 输出 4
print(mb("set_state", "active"))  # 输出 "State set to active"
print(mb.state)  # 输出 "active"
