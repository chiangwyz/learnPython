class Solution:
    def removeTripleDuplicates(self, s: str) -> str:
        """
        在字符串S中执行删除操作，删除连续三个或以上相同的字符。
        重复执行此操作，直到不能再删除为止。
        返回处理后的字符串。
        :param S: str - 由小写字母组成的字符串
        :return: str - 处理后的字符串
        """
        stack = []
        for char in s:
            # 当栈中至少有两个字符时，检查是否需要删除连续的字符
            if len(stack) >= 2 and stack[-1] == char and stack[-2] == char:
                # 如果当前字符与栈顶两个字符相同，则继续检查栈中后续字符是否相同，直到找到不同的字符
                while stack and stack[-1] == char:
                    stack.pop()
            else:
                # 如果不符合删除条件，将当前字符推入栈中
                stack.append(char)
        # 将栈中剩余的字符连接起来，形成最终的字符串
        return ''.join(stack)

# 测试函数
solution = Solution()
input_string = "abbbaaca"
result = solution.removeTripleDuplicates(input_string)
print(result) # ca

input_string2 = "aabbbacbbddfaffffg"
result2 = solution.removeTripleDuplicates(input_string2)
print(result2) # ca

