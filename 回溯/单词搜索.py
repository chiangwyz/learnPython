"""
这个问题可以通过使用深度优先搜索（DFS）算法来解决。
算法的基本思想是从网格中的每一个单元格开始，尝试构造字符串 word。
如果在任意起点能够构造出完整的 word，则返回 true，否则在遍历完所有可能的起点后返回 false。

以下是解题步骤：
1. 遍历网格中的每一个单元格作为起点。
2. 对于每个起点，使用深度优先搜索来尝试构造字符串 word。
3. 在深度优先搜索中，检查当前单元格是否匹配 word 的当前字符。
4. 如果匹配，则递归地在相邻的单元格（上、下、左、右）中继续搜索下一个字符。
5. 为了避免在同一个单元格中重复使用字母，需要在访问单元格时标记它们，访问后再将其恢复。
6. 如果在任何时候，word 被完全匹配，则返回 true。
7. 如果所有起点都无法构造出完整的 word，则返回 false。
"""

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        def dfs(i: int, j: int, k: int):
            # 如果越界，或者字符不匹配，或者该单元格已访问过，则返回False
            if not (0 <= i < len(board)) or not (0 <= j < len(board[0])) or board[i][j] != word[k]:
                return False
            # 如果所有字符都匹配了，则返回True
            if k == len(word) - 1:
                return True

            # 标记当前单元格为已访问
            tmp = board[i][j]
            board[i][j] = '/'
            # 搜索相邻单元格
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            # 恢复当前单元格
            board[i][j] = tmp
            # 返回结果
            return res

        # 遍历网格中的每一个单元格作为起点
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True

        return False

# test
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

solution = Solution()
print(solution.exist(board, word))

board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word1 = "ABCB"
print(solution.exist(board1, word1))

