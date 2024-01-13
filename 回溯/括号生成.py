class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def backtrack(s='', left=0, right=0):
            # 当当前字符串长度达到2*n时，表示一个有效组合已经形成
            if len(s) == 2 * n:
                res.append(s)
                return
            # 如果左括号数量小于n，可以添加左括号
            if left < n:
                backtrack(s + '(', left + 1, right)  # 添加左括号，递归进入下一层
            # 如果右括号数量小于左括号，可以添加右括号
            if right < left:
                backtrack(s + ')', left, right + 1)  # 添加右括号，递归进入下一层

        # 用于存储所有有效的括号组合
        res = []
        # 从空字符串开始递归
        backtrack()
        return res

# test
solution = Solution()

print(solution.generateParenthesis(3))