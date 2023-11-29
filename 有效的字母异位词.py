"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        # 统计 s 中每个字符的出现次数
        for char in s:
            count[char] = count.get(char, 0) + 1

        # 检查 t 中的字符是否在 s 中有相同的出现次数
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] < 0:
                return False

        return True

# 示例测试
sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))  # 输出：True
print(sol.isAnagram("rat", "car"))  # 输出：False



