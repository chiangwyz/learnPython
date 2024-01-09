"""
1. 哈希映射（char_index_map）：存储每个字符遇到的最新索引。
    它有助于检查一个字符是否已经在当前子串中，并相应地更新滑动窗口的起始索引。

2. 滑动窗口（left 和 right 变量）：代表当前正在考虑的子串。left 变量标记窗口的开始，而 right 遍历整个字符串。

3. 更新窗口和计算长度：
    循环遍历字符串，对于每个字符，检查它是否已在当前窗口中（char_index_map[char] >= left）。
    如果是，窗口的左边界移动到这个字符的最后一次出现的右侧，以将其从当前窗口中排除。
    在 char_index_map 中更新每个字符的索引。
    比较当前窗口的长度（right - left + 1）与迄今为止看到的最大长度，并相应地更新最大值。
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 字符及其索引位置的映射
        char_index_map = {}  
        # 滑动窗口的左边界
        left = 0  
        # 最长无重复字符子串的长度
        max_length = 0 

        for right, char in enumerate(s):
            # 如果字符已存在于窗口中，则更新左边界
            if char in char_index_map and char_index_map[char] >= left:
                left = char_index_map[char] + 1
            
            # 更新字符的索引
            char_index_map[char] = right
            # 更新最长子串的长度
            max_length = max(max_length, right - left + 1)
        
        return max_length

# 示例测试
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))  # 输出：3
print(sol.lengthOfLongestSubstring("bbbbb"))  # 输出：1
print(sol.lengthOfLongestSubstring("pwwkew"))  # 输出：3

