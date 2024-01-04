"""
整体思路
这个算法使用了“中心扩展”方法。思想是考虑每个字符（或两个相邻字符）作为潜在的回文中心，然后向两边扩展，直到找到最长的回文子串。

函数细节
1. expandAroundCenter(left: int, right: int) -> str:
    这是一个内嵌的辅助函数，用来实现中心扩展。
    参数 left 和 right 表示开始扩展的位置。
    函数会检查以 left 和 right 为中心的子串是否是回文，如果是，则继续扩展。
    最后返回找到的回文子串。
    
2. 外部循环:
    循环遍历字符串的每个字符，将每个字符（或两个相邻字符）作为回文的中心。
    对于每个中心，使用 expandAroundCenter 函数来找到最长的回文子串。
    首先考虑奇数长度的回文（一个字符为中心）。
    然后考虑偶数长度的回文（两个相邻字符为中心）。
    
3. 如何工作
    对于字符串中的每个位置 i，算法首先尝试找到以 s[i] 为中心的最长奇数长度回文。
    然后，尝试找到以 s[i] 和 s[i+1] 为中心的最长偶数长度回文。
    在每次扩展中，如果找到的回文比之前保存的回文长，则更新最长回文。

4. 举例
    假设 s = "babad"，算法将执行以下步骤：
    
    将 b 作为中心，找到 "b"。
    将 a 作为中心，找到 "aba"。
    将 b 作为中心，找到 "bab"。
    将 a 作为中心，找到 "aba"。
    将 d 作为中心，找到 "d"。
    在这个过程中，还会考虑每两个相邻字符作为中心的情况。
    最后，返回找到的最长回文子串 "bab" 或 "aba"（两者都是正确的，因为它们长度相同）。
"""



class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        找出字符串中最长的回文子串。
        使用中心扩展算法来寻找可能的回文中心，然后向两边扩展。
        """

        def expandAroundCenter(left: int, right: int) -> str:
            """
            从中心向两边扩展，找出最长的回文子串。
            """
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest_palindrome = ""
        for i in range(len(s)):
            # 以 s[i] 为中心的奇数长度回文
            odd_palindrome = expandAroundCenter(i, i)
            if len(odd_palindrome) > len(longest_palindrome):
                longest_palindrome = odd_palindrome

            # 以 s[i] 和 s[i+1] 为中心的偶数长度回文
            even_palindrome = expandAroundCenter(i, i + 1)
            if len(even_palindrome) > len(longest_palindrome):
                longest_palindrome = even_palindrome

        return longest_palindrome

# 测试用例
test_cases = ["babad", "cbbd"]

# 创建 Solution 实例
sol = Solution()

# 计算结果
results = [sol.longestPalindrome(s) for s in test_cases]
results







