"""
与同构字符串差不多
要判断字符串 s 是否遵循模式 pattern 的规律，可以使用字典来建立字符和单词之间的映射关系。
具体来说，我们需要确保 pattern 中的每个字符与 s 中的每个单词之间存在一一对应的关系。实现这个算法可以分为以下几个步骤：
拆分字符串：首先，将字符串 s 按空格拆分成单词。
长度检查：检查 pattern 的长度和拆分后的单词数量是否相等。如果不相等，直接返回 False。
建立映射：遍历 pattern 和 s 的单词列表，对于 pattern 中的每个字符和对应的单词，检查是否能够建立一一对应的映射关系。
双向映射：需要确保映射是双向的。即 pattern 中的每个字符都唯一地映射到 s 中的一个单词，反之亦然。
最终判断：如果所有字符都能成功映射，则返回 True；否则返回 False。
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        word_to_char = {}
        char_to_word = {}

        for char, word in zip(pattern, words):
            if (char in char_to_word and char_to_word[char] != word) or (word in word_to_char and word_to_char[word] != char):
                return False

            word_to_char[word] = char
            char_to_word[char] = word

        return True




