
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:

        # 复制一份board作为更新的基础
        copy_board = [row[:] for row in board]
        
        # 获取板的行数和列数
        rows, cols = len(board), len(board[0])
        
        # 遍历板上的每一个格子
        for row in range(rows):
            for col in range(cols):
                # 计算周围活细胞的数量
                live_neighbors = 0
                for i in range(max(0, row-1), min(rows, row+2)):
                    for j in range(max(0, col-1), min(cols, col+2)):
                        if (i, j) != (row, col) and copy_board[i][j] == 1:
                            live_neighbors += 1
                
                # 根据生命游戏的规则更新当前细胞的状态
                if copy_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = 0
                if copy_board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 1
        
        return board
