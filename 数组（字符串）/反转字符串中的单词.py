"""
Python 中的 split() 方法默认以空白字符（如空格、制表符、换行符等）作为分隔符，并且会自动忽略字符串开头和结尾的空白字符。
当遇到连续的空白字符时，它们被视为一个分隔符。这就是为什么连续的空格在分割时会被忽略，结果中不会有空字符串的原因。
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        # 分割字符串，去除空格
        words = s.split()
        # 反转单词列表
        words.reverse()
        # 用单个空格连接单词，形成新的字符串
        reversed_s = ' '.join(words)
        return reversed_s

# 示例测试
sol = Solution()
print(sol.reverseWords("the sky is blue"))          # 输出："blue is sky the"
print(sol.reverseWords("  hello world  "))          # 输出："world hello"
print(sol.reverseWords("a good   example"))         # 输出："example good a"
