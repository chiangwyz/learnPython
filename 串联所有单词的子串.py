from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []
        
        word_length = len(words[0])
        word_count = len(words)
        substring_length = word_length * word_count
        words_counter = Counter(words)
        result = []

        # 遍历字符串，以每个可能的起始点开始检查
        for i in range(len(s) - substring_length + 1):
            substring = s[i:i + substring_length]  # 取出长度等于所有单词长度总和的子串
            seen_words = []

            # 将子串分割为多个单词长度的小段，并计数
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

