"""
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

代码逻辑
1. res += matrix.pop(0):
    matrix.pop(0) 将移除并返回矩阵的第一行 [1, 2, 3]。
    然后我们将这个行添加到结果列表 res 中。
    matrix =
    [[4, 5, 6]
    [7, 8, 9]]

2. matrix = list(zip(*matrix))[::-1]:
        2.1 *matrix操作会将矩阵中的每一行解包成独立的列表。
        2.2 zip(*matrix)会按列将这些列表合并成元组。在我们的例子中，zip(*matrix)的结果会是：
        [(4, 7), (5, 8), (6, 9)]
        这相当于转置了我们的矩阵（将行转换成列）。
    2.3 接下来，list(zip(*matrix))将这些元组转换成列表。因此，我们得到一个列表的列表，每个内部的列表都代表了原矩阵的一列：
        [[4, 7], [5, 8], [6, 9]]

    2.4 最后，[::-1]将这个列表反转。所以list(zip(*matrix))[::-1]的结果是：
        [[6, 9], [5, 8], [4, 7]]

这就是原矩阵逆时针旋转90度的结果。
在螺旋顺序遍历矩阵的算法中，我们总是取出矩阵的第一行，然后应用这个逆时针旋转操作，
这样下一步我们又可以取出新矩阵的第一行，如此循环，直至矩阵为空。

"""


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        while matrix:
            # 添加第一行并移除
            res += matrix.pop(0)
            # 逆时针旋转矩阵
            matrix = list(zip(*matrix))[::-1]
        return res


# test
sol = Solution()

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result1 = sol.spiralOrder(matrix1)
print("result1 =\n", result1)

matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
result2 = sol.spiralOrder(matrix2)
print("result2 =\n", result2)
