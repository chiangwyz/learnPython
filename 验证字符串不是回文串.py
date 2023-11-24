class Solution:
    def isPalindrome(self, s: str) -> bool:
         # 初始化一个空字符串用来存储筛选后的字符
        good_str = str()
        for char in s:
            # 如果字符是字母或数字
            if char.isalnum():
                # 转换为小写并追加到good_str字符串
                good_str += char.lower()


        # 获取过滤后字符串的长度
        left = 0
        right = len(good_str) - 1
        
        # 双指针法，从两端向中间遍历比较
        while left < right:
            if good_str[left] != good_str[right]:
                return False
            left += 1
            right -= 1

        return True









