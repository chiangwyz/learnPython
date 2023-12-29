"""
罗马数字中没有0这个数字。
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        # 定义罗马数字到整数的映射
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # 初始化整数结果为0
        result = 0
        # 初始化前一个字符代表的数字为0
        prev_value = 0
        
        # 从左到右遍历罗马数字的每一个字符
        for char in s:
            # 获取当前字符代表的整数值
            value = roman_to_int[char]
            # 如果前一个字符代表的数字小于当前字符代表的数字
            # 比如 IV 中的 I 小于 V，应该减去 I 代表的值
            if prev_value < value:
                # 减去二倍前一个数值（因为前面已经加过一次了）
                result += value - 2 * prev_value
            else:
                # 正常情况下加上当前数值
                result += value
            # 更新前一个字符代表的数字为当前数字
            prev_value = value
        
        return result
