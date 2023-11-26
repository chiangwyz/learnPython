
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize data structures for rows, columns, and boxes.
        rows = [{} for _ in range(9)]
        columns = [{} for _ in range(9)]
        boxes = [{} for _ in range(9)]

        # Iterate over each cell in the Sudoku board.
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3) * 3 + j // 3  # Calculate box index.

                    # Keep the current cell value.
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                    # Check if this value has been already seen before.
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False
        return True












