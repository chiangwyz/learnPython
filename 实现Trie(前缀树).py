
class TrieNode:
    # Trie 的节点类
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:

    def __init__(self):
        """
        初始化前缀树对象。
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        向前缀树中插入字符串 word。
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        如果字符串 word 在前缀树中，返回 true；否则，返回 false。
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        """
        如果之前已经插入的字符串 word 的前缀之一为 prefix，返回 true；否则，返回 false。
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

