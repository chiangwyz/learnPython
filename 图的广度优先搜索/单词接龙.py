"""
通过广度优先搜索（BFS）算法来解决。我们的目标是找到从 beginWord 到 endWord 的最短转换序列，并返回这个序列的长度。
我们需要考虑的是，每一步转换只能改变一个字母，并且每个转换后的单词都必须在 wordList 中。

解题思路如下：

1. 首先，检查 endWord 是否在 wordList 中。如果不在，直接返回 0，因为无法完成转换。
2. 创建一个队列来进行广度优先搜索，并将 beginWord 加入到队列中。
3. 对于队列中的每个单词，尝试更改每个位置的字母（从 'a' 到 'z'），并检查是否能在 wordList 中找到。
    如果找到了一个在 wordList 中的单词，并且这个单词是 endWord，则找到了最短路径。
4. 为了避免重复处理相同的单词，从 wordList 中删除找到的单词。
5. 记录转换序列的长度。每处理完队列中的一层单词，序列长度增加1。
6. 如果队列变空，表示没有找到有效地转换序列，返回0。
"""

from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList = set(wordList)  # 转换为集合以便快速查找
        queue = deque([beginWord])  # 使用队列进行广度优先搜索
        length = 1  # 初始长度为1

        while queue:
            for _ in range(len(queue)):  # 遍历当前层的所有单词
                word = queue.popleft()
                if word == endWord:
                    return length

                for i in range(len(word)):  # 尝试更改当前单词的每个字母
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = word[:i] + c + word[i+1:]
                        if next_word in wordList:
                            queue.append(next_word)
                            wordList.remove(next_word)  # 从列表中移除以避免重复处理
            length += 1  # 完成一层，长度加1

        return 0  # 如果队列为空，表示没有找到路径


# test

