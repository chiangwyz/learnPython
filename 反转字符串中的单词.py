class Solution:
    def reverseWords(self, s: str) -> str:
        # 分割字符串，去除空格，并反转单词列表
        words = s.split()
        words.reverse()
        # 用单个空格连接单词，形成新的字符串
        reversed_s = ' '.join(words)
        return reversed_s

# 示例测试
sol = Solution()
print(sol.reverseWords("the sky is blue"))          # 输出："blue is sky the"
print(sol.reverseWords("  hello world  "))          # 输出："world hello"
print(sol.reverseWords("a good   example"))         # 输出："example good a"
