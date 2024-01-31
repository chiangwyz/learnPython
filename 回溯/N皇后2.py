"""
在 N 皇后问题中，需要保证任何两个皇后不能处在同一行、同一列或同一对角线上。下面是这种方法的具体实现步骤：

1. 从第一行开始，尝试在每一列中放置一个皇后。
2. 在放置每一个皇后之前，检查该位置是否安全（即检查是否有其他皇后可以攻击到这个位置）。
3. 如果当前位置安全，将皇后放置在那里，并移动到下一行继续这个过程。
4. 如果在当前行中找不到安全的位置，则回退到上一行，移动那一行的皇后到下一个位置，并重复这个过程。
5. 每找到一个有效的解，就将解的计数增加 1。
"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        def isSafe(row: int, col: int, board: list[int]):
            # 检查列
            for i in range(row):
                if board[i] == col:
                    return False

            # 检查左对角线
            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i] == j:
                    return False

            # 检查右对角线
            for i, j in zip(range(row, -1, -1), range(col, n)):
                if board[i] == j:
                    return False

            return True


        def solve(row: int, board: list[int]):
            if row == n:
                self.count += 1
                return

            for col in range(n):
                if isSafe(row, col, board):
                    board[row] = col
                    solve(row+1, board)
                    # 回溯
                    board[row] = -1

        # 统计可行的方案
        self.count = 0
        # 初始化棋盘
        board = [-1] * n
        # 回溯入口
        solve(0, board)

        # 返回可行方案数
        return self.count








