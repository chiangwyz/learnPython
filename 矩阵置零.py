"""
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。

首先遍历矩阵，标记哪些行和列需要被设置为0。由于我们不能使用额外的空间来存储这些行和列，因此可以使用矩阵的第一行和第一列来存储这些标记。
检查第一行和第一列本身是否需要设置为0，并分别用两个变量is_col和is_row来存储这个信息。
使用第一行和第一列来存储其他行和列是否需要设置为0的信息。如果matrix[i][j]为0，则将matrix[i][0]和matrix[0][j]设为0。
根据第一行和第一列的标记来更新矩阵。从第二行和第二列开始，如果matrix[i][0]或matrix[0][j]为0，则将matrix[i][j]设置为0。
根据is_col和is_row的值更新第一行和第一列。
返回修改后的矩阵。
"""
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        # 记录第一列是否需要设置为0
        is_col = False
        rows, cols = len(matrix), len(matrix[0])

        # 第一次遍历，使用矩阵的第一行和第一列来标记对应的行和列是否需要置0
        for i in range(rows):
            if matrix[i][0] == 0:
                is_col = True  # 第一列需要置0
            for j in range(1, cols):  # 从第二列开始
                if matrix[i][j] == 0:  # 如果发现0
                    # 标记在第一行和第一列
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # 第二次遍历，根据第一行和第一列的标记来更新矩阵
        for i in range(1, rows):
            for j in range(1, cols):
                # 如果第一行或第一列的标记为0，则当前元素设置为0
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # 根据第一行是否需要置0来更新第一行
        if matrix[0][0] == 0:
            for j in range(cols):
                matrix[0][j] = 0
        
        # 根据is_col变量来更新第一列
        if is_col:
            for i in range(rows):
                matrix[i][0] = 0







