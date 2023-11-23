class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 首先，我们去除字符串s末尾的所有空格，以确保不会干扰到最后一个单词的长度计算
        s = s.rstrip()
        # 找出最后一个空格的位置，这个位置之后的字符串就是最后一个单词
        last_space_index = s.rfind(' ')
        # 返回最后一个单词的长度，即整个字符串的长度减去最后一个空格位置之后的长度
        return len(s) - last_space_index - 1

# 示例代码测试
sol = Solution()
print(sol.lengthOfLastWord("Hello World"))  # 输出应该是 5
print(sol.lengthOfLastWord("   fly me   to   the moon  "))  # 输出应该是 4
print(sol.lengthOfLastWord("luffy is still joyboy"))  # 输出应该是 6
