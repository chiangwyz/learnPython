"""
这个问题是一个典型的字母板上的单词搜索问题，可以通过回溯法（Backtracking）来解决。
首先，我们需要遍历字母板的每个单元格，然后从每个单元格开始，尝试构建单词并检查它是否在单词列表中。
由于同一个单元格的字母不能在单词中重复使用，我们需要在递归过程中跟踪已访问的单元格。
下面是解决方案的大致步骤和代码实现：

1. 构建字典树（Trie）：由于我们需要频繁检查当前构建的单词是否在单词列表中，使用字典树可以提高这一过程的效率。
2. 回溯搜索：对于字母板上的每个单元格，我们尝试进行深度优先搜索（DFS），探索所有可能的单词组合。
3. 检查单词：在构建单词的过程中，我们利用字典树来检查当前单词是否是单词列表中的单词的前缀。
  如果是，则继续搜索；如果不是，回溯到上一个单元格。
4. 避免重复使用单元格：在搜索过程中，我们需要标记当前正在使用的单元格，以避免重复使用它。
5. 收集结果：一旦找到一个有效的单词，就将其添加到结果列表中。
"""

from collections import defaultdict

class TreeNode:
    def __init__(self):
        self.children = defaultdict(TreeNode)
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, words: str):
        node = self.root
        for char in words:
            node = node.children[char]
        node.is_end_of_word = True

    def searchPrefix(self, prefix: str):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        
        return node

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(board: List[List[str]], node: TreeNode, i: int, j: int, path: List[str], res: set()):
            # 如果当前节点表示一个单词的末尾，将其添加到结果集中  
            if node.is_end_of_word:
                res.add(path)
                # 避免重复添加单词
                node.is_end_of_word = False

            # 检查坐标是否越界
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return

            # 提取当前单元格的字符
            tmp = board[i][j]
            # 如果字符不在当前 TreeNode 节点的子节点中，返回
            if tmp not in node.children:
                return

            # 标记当前单元格的字符，以避免在同一个单词中重复使用
            board[i][j] = "#"
            # 对当前单元格的所有相邻单元格进行深度优先搜索
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                dfs(board, node.children[tmp], x, y, path+tmp, res)
            # 恢复当前单元格的字符  
            board[i][j] = tmp

        # 插入word
        treenode = Trie()
        for word in words:
            treenode.insert(word)

        res = set()
        # 遍历字母板的每一个单元格
        for i in range(len(board)):
            for j in range(len(board[0])):
                # 从每个单元格开始进行深度优先搜索
                dfs(board, treenode.root, i, j, "", res)

        return list(res)


