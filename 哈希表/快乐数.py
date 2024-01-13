"""
def get_next(number):
这是一个定义在 isHappy 方法内部的辅助函数，用于计算给定数字每位数平方和。

while number > 0:
这个循环用于处理数字的每一位，直到数字变为 0。

number, digit = divmod(number, 10)
divmod 函数同时返回商和余数。这里用于获取 number 的最后一位数字（余数）和剩下的部分（商）。
number 是商，表示去除最后一位后剩下的数字。
digit 是余数，即当前处理的最后一位数字。

total_sum += digit ** 2
** 表示幂运算，这里用于计算当前位数字的平方，并累加到 total_sum。

seen = set()
这行代码初始化一个空集合 seen，用于存储所有已经出现过的平方和，以便检测循环。

while n != 1 and n not in seen:
这个循环条件确保当数字变为 1 或者发现数字的平方和开始重复时停止。

seen.add(n)
向集合 seen 中添加当前数字的平方和。

return n == 1
如果 n 最终等于 1，则说明它是快乐数，返回 True。如果 n 因为进入循环而跳出循环，则不是快乐数，返回 False。
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number: int) -> int:
            # 计算下一个数字的平方和
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        # 存储所有已经出现过的平方和
        seen = set()  
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1

# test
solution = Solution()
print(solution.isHappy(19))
