"""
解决 n 皇后问题的关键是要遵守国际象棋中皇后的移动规则，即任两个皇后不能处在同一行、同一列或同一对角线上。
使用回溯法来解决这个问题。

思路如下：
1. 初始化棋盘：首先，创建一个 n×n 的棋盘，开始时每个位置都是空的。
2. 选择位置放置皇后：从第一行开始，尝试在每一列中放置一个皇后。
3. 检查冲突：在放置每个皇后之前，检查当前位置是否与已放置的皇后在同一列、同一行或同一对角线上。
    如果是，则当前列不可放置皇后，尝试下一列。
4. 回溯：如果当前行的所有列都不能放置皇后，回溯到上一行，改变皇后的位置。
5. 递归：对每一行重复以上步骤。
6. 记录解决方案：每次在棋盘上成功放置了 n 个皇后，就记录下当前棋盘的布局作为一个解决方案。
"""


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        def could_place(row: int, col: int):
            """
            检查在(row, col)位置放置皇后是否会有冲突
            """
            return not (cols[col] + hill_diagonals[row - col] + dale_diagonals[row + col])

        def place_queen(row: int, col: int):
            """
            放置皇后，并更新辅助变量
            """
            queens.add((row, col))
            cols[col] = 1
            hill_diagonals[row - col] = 1
            dale_diagonals[row + col] = 1

        def remove_queen(row: int, col: int):
            """
            移除皇后，并恢复辅助变量
            """
            queens.remove((row, col))
            cols[col] = 0
            hill_diagonals[row - col] = 0
            dale_diagonals[row + col] = 0

        def add_solution():
            """
            记录解决方案
            """
            solution = []
            for _, col in sorted(queens):
                solution.append('.' * col + 'Q' + '.' * (n - col - 1))
            output.append(solution)

        def backtrack(row: int = 0):
            """
            回溯递归函数
            """
            for col in range(n):
                if could_place(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        add_solution()
                    else:
                        backtrack(row + 1)
                    remove_queen(row, col)

        cols = [0] * n  # 表示列的占用情况
        hill_diagonals = [0] * (2 * n - 1)  # 表示主对角线的占用情况
        dale_diagonals = [0] * (2 * n - 1)  # 表示副对角线的占用情况
        queens = set()  # 用于存放已经放置的皇后位置
        output = []  # 存放所有的解决方案
        backtrack()
        return output
