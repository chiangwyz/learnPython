"""
解决方案思路：

计算单个单词的长度 word_length 和整个单词列表的总长度 substring_length。
用一个计数器 words_counter 来计数 words 列表中每个单词出现的次数。
遍历主字符串 s，对于每个可能的起始点，取出长度等于 substring_length 的子串。
把这个子串进一步分割成多个长度等于 word_length 的小段，计数这些小段中每个单词出现的次数。
如果分割后的单词计数与 words_counter 相同，说明这个子串是由单词列表 words 中的单词按某种顺序串联而成的，记录下这个子串的起始索引。
为什么可以这样做：

由于所有单词长度相同，我们可以通过分割检查子串是否包含了 words 列表中的所有单词。
通过比较计数器，我们可以确保子串包含的单词与 words 列表中的单词完全一致，既没有多也没有少。

example_words = ["foo", "bar"]
example_words_counter = Counter(example_words)
print("example_words_counter = ", example_words_counter)
# 输出结果
example_words_counter =  Counter({'foo': 1, 'bar': 1})
"""
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        # 单词的长度（假设所有单词长度相同）
        word_length = len(words[0])
        # 单词的数量
        word_count = len(words)
        # 所有单词组成的字符串的总长度
        substring_length = word_length * word_count
        # 对单词列表进行计数
        words_counter = Counter(words)
        # 存储结果的列表
        result = []

        # 遍历字符串，检查每个可能的起始点
        for i in range(len(s) - substring_length + 1):
            # 获取当前起始点的子串
            substring = s[i:i + substring_length]
            # 用于记录已见单词的列表
            seen_words = []

            # 遍历子串，每次取出一个单词的长度
            for j in range(0, substring_length, word_length):
                word = substring[j:j + word_length]
                seen_words.append(word)

            # 如果分割后的单词列表与原单词列表的计数相同，记录起始索引
            if Counter(seen_words) == words_counter:
                result.append(i)

        return result


# 示例解释
sol = Solution()
example_s = "barfoothefoobarman"
example_words = ["foo", "bar"]
# 输出结果
example_result = sol.findSubstring(example_s, example_words)
print(f"在字符串 '{example_s}' 中，单词列表 {example_words} 的串联子串的起始索引为：{example_result}")

# 逐步解释
# 对于字符串 "barfoothefoobarman" 和单词列表 ["foo", "bar"]:
# - "barfoo" 是第一个有效的串联子串，起始索引为 0。
# - "foobar" 是第二个有效的串联子串，起始索引为 9。
# 因此，结果是 [0, 9]。

