class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 如果 x 是负数，它不可能是回文数
        if x < 0:
            return False
        
        # 将整数转换为字符串
        str_x = str(x)
        
        # 比较字符串及其反转后的字符串
        # 如果两者相等，表示 x 是回文数
        return str_x == str_x[::-1]

# 测试函数
sol = Solution()
example1 = sol.isPalindrome(121)  # 应该返回 True，因为 121 是回文数
example2 = sol.isPalindrome(-121)  # 应该返回 False，因为 -121 不是回文数
example3 = sol.isPalindrome(10)  # 应该返回 False，因为 10 不是回文数
