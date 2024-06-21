"""
浅拷贝会创建一个新的对象，但不递归地复制其内容。
对于容器对象（如列表、字典等），浅拷贝会创建一个新的容器对象，并将原始容器中的元素引用复制到新容器中。
这意味着新容器和原始容器中的元素是共享的，即它们指向相同的内存地址。
"""


import copy

original_list = [[1, 2, 3], [4, 5, 6]]
shallow_copied_list = copy.copy(original_list)

# 浅拷贝后，两者的ID不同，表示是不同的对象
print("original_list id =", id(original_list))
print("shallow_copied_list id =", id(shallow_copied_list))
print(id(original_list) == id(shallow_copied_list))  # 输出 False

# 列表中的元素ID相同，表示是共享的
print("original_list[0] id =", id(original_list[0]))
print("shallow_copied_list[0] id =", id(shallow_copied_list[0]))
print(id(original_list[0]) == id(shallow_copied_list[0]))  # 输出 True
print(id(original_list[1]) == id(shallow_copied_list[1]))  # 输出 True

# 修改浅拷贝中的一个元素
shallow_copied_list[0][0] = 100

# 原始列表中的对应元素也会改变
print(original_list)  # 输出 [[100, 2, 3], [4, 5, 6]]
print(shallow_copied_list)  # 输出 [[100, 2, 3], [4, 5, 6]]


