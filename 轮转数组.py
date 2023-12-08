"""
对 k 进行取模操作：由于将数组 nums 旋转 k 次与旋转 k % len(nums) 次效果相同，
所以函数首先将 k 减少到数组长度范围内的等效值。这一步在 k 大于数组长度的情况下非常有用。

拓展知识：
在Python中，reverse 和 reversed 是两个不同的方法，它们都用于反转序列（例如列表或字符串），但它们的工作方式和用途有所不同：

1. reverse 方法：
reverse 是列表（list）对象的一个方法，它用于原地反转列表，即直接在原列表上进行操作，不创建新的列表。
它不返回任何值（或者说返回 None），因为它直接修改了原列表。
使用方法：list.reverse()
适用于：仅适用于列表。
举例：如果有一个列表 a = [1, 2, 3]，调用 a.reverse() 后，a 将变为 [3, 2, 1]。

2. reversed 函数：
reversed 是Python的内置函数，它用于返回一个反转的迭代器。
它不会改变原序列，而是生成一个新的反转后的迭代器，可以用于任何可迭代的对象，例如列表、元组、字符串等。
使用方法：reversed(seq)
适用于：任何可迭代的对象。
举例：如果有一个列表 a = [1, 2, 3]，调用 reversed(a) 将返回一个迭代器，可以使用 list(reversed(a)) 将其转换为列表 [3, 2, 1]，但原列表 a 保持不变。

总结：
reverse 是一个修改列表的方法，它会改变原列表的顺序。
reversed 是一个返回新迭代器的函数，不会改变原序列，可以用于任何可迭代的对象。
"""

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 由于轮转k次和轮转n次效果相同，其中n是数组长度，我们使用k对数组长度取模
        k = k % len(nums)
        # 首先，将整个数组翻转
        nums.reverse()
        # 然后，翻转前k个元素
        nums[:k] = reversed(nums[:k])
        # 最后，翻转剩下的元素
        nums[k:] = reversed(nums[k:])
