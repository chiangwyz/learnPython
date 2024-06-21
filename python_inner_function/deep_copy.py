"""
深拷贝会递归地复制对象及其包含的所有对象。
对于容器对象，深拷贝会创建一个新的容器对象，并递归地复制原始容器中的所有元素及其包含的内容。
"""

import copy

original_list = [[1, 2, 3], [4, 5, 6]]
deep_copied_list = copy.deepcopy(original_list)

# 深拷贝后，两者的ID不同，表示是不同的对象
print("original_list id =", id(original_list))
print("deep_copied_list id =", id(deep_copied_list))
print(id(original_list) == id(deep_copied_list))  # 输出 False

# 列表中的元素ID也不同，表示不再共享
print("original_list[0] id =", id(original_list[0]))
print("deep_copied_list[0] id =", id(deep_copied_list[0]))
print(id(original_list[0]) == id(deep_copied_list[0]))  # 输出 False
print(id(original_list[1]) == id(deep_copied_list[1]))  # 输出 False

# 修改深拷贝中的一个元素
deep_copied_list[0][0] = 100

# 原始列表中的对应元素不会改变
print(original_list)  # 输出 [[1, 2, 3], [4, 5, 6]]
print(deep_copied_list)  # 输出 [[100, 2, 3], [4, 5, 6]]

