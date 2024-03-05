import copy

# 浅拷贝示例
original_list = [1, 2, [3, 4]]
shallow_copied_list = original_list.copy()
shallow_copied_list[2][0] = "a"

# 深拷贝示例
original_list_deep = [1, 2, [3, 4]]
deep_copied_list = copy.deepcopy(original_list_deep)
deep_copied_list[2][0] = "b"

print(original_list)  # 输出: [1, 2, ['a', 4]]，显示原始列表的子列表被修改了
print(shallow_copied_list)  # 输出: [1, 2, ['a', 4]]，显示原始列表的子列表被修改了
print(original_list_deep)  # 输出: [1, 2, [3, 4]]，显示原始列表的子列表没有被修改
