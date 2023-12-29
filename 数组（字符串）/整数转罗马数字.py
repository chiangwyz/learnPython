class Solution:
    def intToRoman(self, num: int) -> str:
        # 罗马数字的表示，从大到小
        value_symbols = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

        # 初始化罗马数字字符串为空
        roman_numeral = ''  
        
        # 遍历每个罗马数字和对应的整数值
        for value, symbol in value_symbols:
            # 当num大于等于当前值时，表示可以使用当前的罗马数字
            while num >= value:
                # num减去当前的值
                num -= value  
                # 将对应的罗马数字加到结果字符串中
                roman_numeral += symbol  
        # 返回罗马数字字符串
        return roman_numeral  

