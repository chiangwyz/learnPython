"""
一些细节：
在 Python 中，// 运算符用于进行整除运算，即除法后向下取整到最近的整数。
对于 box_index 的计算，它是根据当前的行 i 和列 j 来确定每个单元格所在的 3x3 宫格的索引。这是数独的一个常用技巧。
这里是具体如何计算的：
1. i // 3 会将数独的行索引 i 分成三部分（0、1、2），每部分对应一组宫格的行。
2. (i // 3) * 3 将这个行组索引转换为宫格的起始行索引。
3. j // 3 会将数独的列索引 j 同样分成三部分，每部分对应一组宫格的列。
4. (i // 3) * 3 + j // 3 最终确定了单元格在哪个宫格中。

例如：
1. 对于位于 i = 4 和 j = 7 的单元格，宫格索引计算如下：
2. i // 3 是 4 // 3，等于 1，表示它在第二组行（因为索引从0开始）。
3. (i // 3) * 3 是 1 * 3，等于 3，表示宫格的起始行是第4行。
4. j // 3 是 7 // 3，等于 2，表示它在第三组列。
5. (i // 3) * 3 + j // 3 是 3 + 2，等于 5，所以单元格位于第6个宫格（因为索引从0开始）。

字典的 get 方法用于获取字典中 num 键对应的值。如果 num 不存在，则返回默认值 0。然后，这个值会加1，更新字典中 num 的计数。
因此，rows[i][num] = rows[i].get(num, 0) + 1 这行代码的含义是：
查找 rows[i] 这个字典里 num 这个键的值，如果没有找到 num 这个键，就返回0。
将这个值加1，然后将结果重新赋值给 rows[i] 这个字典里的 num 键，相当于更新了 num 这个数字在第 i 行出现的次数。
"""
from collections import defaultdict

# Python 函数来验证数独是否有效
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # 使用 defaultdict 初始化数独的每一行、每一列和每个3x3宫
        rows = [defaultdict(int) for _ in range(9)]
        columns = [defaultdict(int) for _ in range(9)]
        boxes = [defaultdict(int) for _ in range(9)]
    
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
solution = Solution()
isValid = solution.isValidSudoku(board_example)
print(isValid)  # 输出：True
