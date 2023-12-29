"""
1. 初始化行容器：创建一个列表 rows，用于存储每行的字符。
    列表的长度为 numRows 和字符串长度 s 中的最小值，因为行数不会超过字符串的长度。
2. 遍历字符串：遍历字符串 s 中的每个字符。
3. 计算行索引：使用两个变量 curRow 和 goingDown 来确定字符应该放在哪一行。
    curRow 表示当前行的索引。
    goingDown 表示当前遍历的方向，向下或向上。
4. 放置字符：将当前字符添加到 rows[curRow] 中。
5. 更新行索引和方向：
    如果到达了第一行或最后一行，改变方向（goingDown 取反）。
    根据方向更新 curRow（向下则增加，向上则减少）。
6. 连接行字符串：最后，将 rows 中的所有字符串连接起来，形成最终结果。
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 如果行数为1或者字符串长度小于行数，直接返回原字符串
        if numRows == 1 or numRows >= len(s):
            return s

        # 初始化行容器
        rows = ['' for _ in range(min(numRows, len(s)))]
        curRow = 0
        goingDown = False

        # 遍历字符串
        for c in s:
            rows[curRow] += c
            # 如果到达第一行或最后一行，改变方向
            if curRow == 0 or curRow == numRows - 1:
                if goingDown:
                    goingDown = False
                else:
                    goingDown = True
            # 根据方向更新行索引
            if goingDown:
                curRow += 1
            else:
                curRow -= 1
        
        # 连接字符串
        return ''.join(rows)
