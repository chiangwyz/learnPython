class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        while matrix:
            # 添加第一行并移除
            res += matrix.pop(0)
            # 逆时针旋转矩阵
            matrix = list(zip(*matrix))[::-1]
        return res









