import numpy as np

# 创建一个一维数组
a = np.array([0, 2, 0, 3, 4])

# 使用 np.nonzero 找到非零元素的索引
indices = np.nonzero(a)

print("indices =", indices)
# 输出: (array([1, 3, 4]),)
# 解释: 返回一个元组，其中包含一个数组。数组中的值是非零元素的索引。

print("indices[0] =", indices[0])
print("indices[0][0] =", indices[0][0])

# 直接获取非零元素
non_zero_elements = a[indices]
print("non_zero_elements =", non_zero_elements)
# 输出: [2 3 4]


# 创建一个布尔数组
b = np.array([True, False, True, False, True])

# 使用 np.nonzero 找到值为 True 的元素的索引
indices = np.nonzero(b)

print("indices =", indices)
print("indices[0] =", indices[0])
print("indices[0][0] =", indices[0][0])
# 输出: (array([0, 2, 4]),)
# 解释: 返回一个元组，其中包含一个数组。数组中的值是 True 元素的索引。

# 直接获取值为 True 的元素
true_elements = b[indices]
print(true_elements)
print("true_elements =", true_elements)
print("true_elements[0] =", true_elements[0])
# 输出: [ True  True  True]


# 创建一个二维数组
c = np.array([[1, 0, 3],
              [0, 4, 0],
              [5, 0, 6]])

# 使用 np.nonzero 找到非零元素的索引
indices = np.nonzero(c)

print("c indices =", indices)
print("c indices[0] =", indices[0])
# 输出: (array([0, 0, 1, 2, 2]), array([0, 2, 1, 0, 2]))
# 解释: 返回两个数组，第一个数组表示行索引，第二个数组表示列索引。
#       例如，(0, 0) 表示元素 1 的位置，(0, 2) 表示元素 3 的位置。

# 直接获取非零元素
non_zero_elements = c[indices]
print(non_zero_elements)
# 输出: [1 3 4 5 6]
