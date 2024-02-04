"""
可以利用一个重要的观察点：对于区间[left,right]内所有数字的按位与结果，其实是找出left和right的公共前缀部分。
因为一旦left到right之间的数字在某一位上有0和1的差异，那么该位的按位与结果一定是0。
而只有在两个数的最高位到某一位之间完全相同，即它们的公共前缀，才会在按位与操作中保留下来。

解题步骤如下：
1. 我们将left和right同时右移，直到它们相等，记录下移动的步数。这个过程是为了找到left和right的公共前缀。
2. 当left和right相等时，我们找到了它们的公共前缀，然后将left或right左移之前记录的步数，恢复到原来的长度，
    这时的数就是原区间内所有数按位与的结果。
3. 返回最后的结果。

"""

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # 移动次数，用于记录left和right对齐需要右移的次数
        shift = 0
        # 当left和right不相等时，持续右移
        while left != right:
            left >>= 1  # left右移
            right >>= 1  # right右移
            shift += 1  # 记录移动次数
        # 最后将left或right左移之前记录的步数，恢复到原来的长度
        return left << shift
