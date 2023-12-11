"""
对于计算非负整数 

x 的算术平方根，我们可以使用一种叫做“二分查找”的方法。这个方法不使用任何内置的指数函数或算符，比如 pow(x, 0.5) 或 x ** 0.5。
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        # 当 x 小于 2 时，直接返回 x 本身
        if x < 2:
            return x

        # 使用二分查找法来寻找平方根
        # 初始化左右边界
        left, right = 2, x // 2
        
        # 当左边界不超过右边界时进行循环
        while left <= right:
            # 计算中间值
            mid = (left + right) // 2
            # 计算中间值的平方
            squared = mid * mid

            # 根据中间值的平方与 x 的比较结果调整边界
            if squared > x:
                right = mid - 1
            elif squared < x:
                left = mid + 1
            else:
                # 找到精确的平方根，直接返回
                return mid

        # 当无法找到精确的平方根时，返回最接近的整数值（向下取整）
        return right
