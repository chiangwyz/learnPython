class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        # 复制一份board作为更新的基础
        copy_board = [row[:] for row in board]
        
        # 获取板的行数和列数
        rows = len(board)
        cols = len(board[0])
        
        # 遍历板上的每一个格子
        for row in range(rows):
            for col in range(cols):
                # 计算周围活细胞的数量
                live_neighbors = 0
                """
                (i, j) != (row, col) 这样的语句是用来比较两个元组是否不相等。
                这里，(i, j) 和 (row, col) 都是元组，元组是 Python 中的一种数据结构，用来存储有序的元素集合。
                这个比较是逐元素进行的。首先比较元组中的第一个元素（i 和 row），如果它们不相等，那么整个元组就被认为是不相等的。
                如果第一个元素相等，则比较第二个元素（j 和 col）。只有当两个元组中的所有对应元素都相等时，这两个元组才被认为是相等的。
                """
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
