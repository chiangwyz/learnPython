"""
如果要在数组的前后都添加给定的数值，可以使用 np.pad() 函数，并指定填充值（constant_values 参数）。下面是如何实现这一操作的示例。
假设你有一个数组 arr，并且你想在数组的开始和末尾分别填充指定的数值 value_start 和 value_end。
"""

import numpy as np

# 原始数组
arr = np.array([1, 2, 3, 4, 5])

# 要填充的数值
value_start = 9
value_end = 8

# 填充长度
num_pad_start = 2
num_pad_end = 3

# [1 2 3 4 5]
print("填充前 = ", arr)

# 使用 np.pad() 填充数组前后的值
padded_arr = np.pad(arr, (num_pad_start, num_pad_end), 'constant', constant_values=(value_start, value_end))

# [9 9 1 2 3 4 5 8 8 8]
print("填充后 = ", padded_arr)
