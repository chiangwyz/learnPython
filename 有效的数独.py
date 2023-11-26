# Python 函数来验证数独是否有效
def isValidSudoku(board):
    # 为数独的每一行、每一列和每个3x3宫初始化字典
    rows = [{} for _ in range(9)]
    columns = [{} for _ in range(9)]
    boxes = [{} for _ in range(9)]

    # 遍历数独的每一个单元格
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            # 只检查已填的单元格
            if num != '.':
                num = int(num)
                # 计算当前单元格所在的3x3宫索引
                box_index = (i // 3) * 3 + j // 3

                # 将当前单元格的数字添加到对应的行、列和宫字典中
                rows[i][num] = rows[i].get(num, 0) + 1
                columns[j][num] = columns[j].get(num, 0) + 1
                boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                # 检查当前数字在对应的行、列和宫是否出现了多次
                if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                    return False

    return True

# 示例数独棋盘
board_example = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

# 检查示例数独棋盘是否有效
isValid = isValidSudoku(board_example)
print(isValid)  # 输出：True
