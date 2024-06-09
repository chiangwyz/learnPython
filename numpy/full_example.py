"""
np.full(shape, fill_value):
shape: 要创建的数组的形状。可以是一个整数或一个元组。
fill_value: 数组中每个元素的初始值。
"""

import numpy as np


class Example:
    def __init__(self, num_tasks):
        self.num_tasks = num_tasks
        self.used_tasks = np.full(self.num_tasks, False)

    def use_task(self, task_id):
        if 0 <= task_id < self.num_tasks:
            self.used_tasks[task_id] = True


# 创建 Example 实例，假设有 5 个任务
example = Example(5)
print(example.used_tasks)  # 输出: [False False False False False]

# 使用任务 2
example.use_task(2)
print(example.used_tasks)  # 输出: [False False  True False False]
