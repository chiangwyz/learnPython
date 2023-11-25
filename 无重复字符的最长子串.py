
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}  # 字符及其索引位置的映射
        left = 0  # 滑动窗口的左边界
        max_length = 0  # 最长无重复字符子串的长度

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

