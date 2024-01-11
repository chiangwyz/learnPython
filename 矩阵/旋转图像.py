"""
非常巧妙的解法，
这也是使用Python的优势。
先转置，再反转每一行。
"""

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        # 获取矩阵的维度，即n x n
        n = len(matrix)

        # 转置矩阵
        for i in range(n):
            for j in range(i, n):
                # 交换索引为(i, j)和(j, i)的元素
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        # 反转每一行
        for i in range(n):
            matrix[i].reverse()
