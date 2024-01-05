class Solution:
    def removeTripleDuplicates(self, s: str) -> str:
        """
        在字符串S中执行删除操作，删除连续三个相同的字符。
        重复执行此操作，直到不能再删除为止。
        返回处理后的字符串。
        :param S: str - 由小写字母组成的字符串
        :return: str - 处理后的字符串
        """
        stack = []
        for char in s:
            # 检查栈顶是否有两个连续且相同的字符
            if len(stack) >= 2 and stack[-1] == char and stack[-2] == char:
                # 如果找到了三个连续的字符，则弹出栈顶的两个字符
                stack.pop()
                stack.pop()
            else:
                # 否则，将当前字符推入栈中
                stack.append(char)
        # 将栈中剩余的字符连接起来，形成最终的字符串
        return ''.join(stack)

# 测试函数
input_string = "abbbaaca"
solution = Solution()
result = solution.removeTripleDuplicates(input_string)
print(result)
