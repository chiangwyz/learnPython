"""
杨辉三角，经典的问题，需要注意细节处为两个for循环。
"""
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 0:
            return []

        # 初始化杨辉三角
        triangle = [[1]*(i+1) for i in range(numRows)]

        # 从第三行开始填充杨辉三角
        for i in range(2, numRows):
            for j in range(1, i):
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

        return triangle



