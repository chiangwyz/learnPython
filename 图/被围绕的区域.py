"""
这个问题可以通过深度优先搜索（DFS）算法来解决。
我们的目标是找到所有被 'X' 完全包围的 'O' 并将它们替换为 'X'。
然而，直接这样做会很复杂，因为我们需要检查每个 'O' 是否被 'X' 完全包围。
一个更简单的方法是先找出所有不被 'X' 完全包围的 'O'（即那些在边界上或与边界上的 'O' 相连的 'O'），并将它们标记为另一个字符（比如 'A'）。
之后，我们遍历整个矩阵，将所有剩余的 'O' 替换为 'X'，然后再将标记为 'A' 的字符恢复为 'O'。

解题步骤如下：
1. 遍历矩阵的四个边界，对于每个在边界上的 'O'，使用 DFS 算法标记所有与之相连的 'O'。
2. 遍历整个矩阵，将所有的 'O' 替换为 'X'。
3.  再次遍历整个矩阵，将所有的 'A' 恢复为 'O'。
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])

        # DFS 函数，用于标记所有不在边界上且不与边界上的 'O' 相连的 'O'
        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != 'O':
                return
            board[i][j] = 'A'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # 遍历四个边界
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)

        # 替换所有的 'O' 为 'X'，并将 'A' 恢复为 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'


