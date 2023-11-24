class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 双指针初始化为两个字符串的起始位置
        pointer_s, pointer_t = 0, 0
        # 获取两个字符串的长度
        len_s, len_t = len(s), len(t)

        # 当两个指针都未达到各自字符串的末尾时，进行循环
        while pointer_s < len_s and pointer_t < len_t:
            # 如果两个指针指向的字符相等，s的指针右移
            if s[pointer_s] == t[pointer_t]:
                pointer_s += 1
            # t的指针始终右移
            pointer_t += 1
        
        # 如果s的指针达到了末尾，说明s是t的子序列
        return pointer_s == len_s

# 示例测试
sol = Solution()
print(sol.isSubsequence("abc", "ahbgdc"))  # 输出：True
print(sol.isSubsequence("axc", "ahbgdc"))  # 输出：False

