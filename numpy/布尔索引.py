import numpy as np

test_array = np.array([0., 19., 0., 0., 0., 0., 0., 0., 0., 0., 22., 10., 16., 0., 10., 0., 10., 0., 0., 0., 0., 0., 0., 0., 11.])
index = [i for i in range(len(test_array)) if test_array[i] > 0]

# [1, 10, 11, 12, 14, 16, 24]
print("index = \n{}".format(index))

# 使用index数组作为索引来选择 test_array 中的元素
selected_elements = test_array[index]
# [19. 22. 10. 16. 10. 10. 11.]
print("selected_elements = \n{}".format(selected_elements))


# 多维数组也可以，以二维数组为例
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
index = [0, 2]

# 选择第一行和第三行
selected_rows = arr[index]
"""
[[1 2 3]
 [7 8 9]]
"""
print("selected_rows = \n{}".format(selected_rows))

