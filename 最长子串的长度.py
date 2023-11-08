"""
我们使用一个字典 char_index_map 来记录每个字符最后一次出现的位置。
我们遍历字符串 s，使用变量 i 来表示当前位置，char 表示当前字符。
如果 char 出现在 char_index_map 中，并且这个字符的索引大于等于滑动窗口的起始位置 start，说明我们找到了一个重复的字符，需要更新窗口的起始位置 start 为当前字符上一次出现位置的下一位置。
每次迭代时，我们都会更新字符在 char_index_map 中的位置，然后计算当前窗口的长度 i - start + 1，并用它来更新 max_length。
最后返回 max_length 作为结果。这个算法的时间复杂度为 O(n)，因为每个字符只被访问一次。
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 定义一个字典用来存储字符最后一次出现的索引
        char_index_map = {}
        # 定义一个变量用来保存最长子串的长度
        max_length = 0
        # 定义滑动窗口的起始位置
        start = 0

        # 遍历字符串
        for i, char in enumerate(s):
            # 如果字符已经在字典中，并且这个字符的索引大于或等于滑动窗口的起始位置
            # 则更新滑动窗口的起始位置
            if char in char_index_map and char_index_map[char] >= start:
                start = char_index_map[char] + 1
            # 更新字符最后一次出现的索引
            char_index_map[char] = i
            # 更新最长子串的长度
            max_length = max(max_length, i - start + 1)
        
        # 返回最长子串的长度
        return max_length
