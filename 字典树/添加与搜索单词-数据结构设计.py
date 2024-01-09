"""
要实现这个数据结构，最合适的是使用一种称为“字典树”（Trie）的数据结构。
字典树是一种树形结构，非常适合用于处理字符串集合，尤其是用于前缀匹配和模式匹配。
在这种情况下，我们需要稍微修改标准的字典树来处理包含.的模式匹配。

以下是实现步骤：
1. 初始化（__init__）: 创建字典树的根节点。这个节点不包含字符，但它将是所有单词的起始点。
2. 添加新单词（addWord）: 对于每个新单词，我们从根节点开始，对每个字符进行遍历。
  如果字符不存在，则在当前节点创建一个新的子节点。然后，移动到这个子节点并继续处理下一个字符。
  在单词的最后一个字符后，我们标记这个节点为一个单词的结束。
3. 搜索（search）: 这是这个数据结构的关键部分。当我们搜索一个单词时，我们从根节点开始遍历。如果遇到.字符，我们必须检查当前节点的所有子节点。
  如果是普通字符，我们就直接移动到对应的子节点。如果在任何时刻，所需的子节点不存在，我们返回False。
  如果我们到达单词的末尾，我们检查当前节点是否被标记为一个单词的结束。
"""

class TreeNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TreeNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(j: int, root: TreeNode):
            node = root
            for i in range(j, len(word)):
                char = word[i]
                if char == ".":
                    for child in node.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if char not in node.children:
                        return False
                    node = node.children[char]
            return node.is_end_of_word
        
        return dfs(0, self.root)
