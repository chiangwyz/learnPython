"""
要实现 myAtoi(string s) 函数，我们需要遵循以下步骤：

1. 去除前导空格：使用字符串的 strip() 方法去除前导空格。
2. 检查正负号：检查字符串的第一个字符是否为 '+' 或 '-'。如果是，则记录下正负号，并从下一字符开始处理数字。
3. 处理数字：遍历剩下的字符，直到遇到非数字字符或字符串结束。在这个过程中，将每个数字字符转换成整数并累加到结果中。
4. 处理边界情况：确保结果在 32 位有符号整数范围内。如果结果超出这个范围，则需要将其修正为边界值。
5. 返回结果：返回最终的整数值。
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        # 初始化结果为 0 和符号为 1
        result = 0
        sign = 1

        # 去除前导空格
        s = s.strip()

        # 检查是否为空字符串
        if not s:
            return 0

        # 检查正负号
        if s[0] in ['-','+']:
            sign = -1 if s[0] == '-' else 1
            s = s[1:]

        # 检查正负号，并更新字符串 s
        for char in s:
            if char.isdigit():
                # 将字符转换为数字并累加到结果中
                result = result * 10 + int(char)
            else:
                # 遇到非数字字符，停止处理
                break

        # 处理边界情况
        result = result * sign
        if result < -2**31:
            return -2**31
        if result > 2**31 - 1:
            return 2**31 - 1

        # 返回最终结果
        return result
