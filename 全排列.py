"""
使用示例1（nums = [1,2,3]）来详细解释代码的运行过程。我们考虑一个递归函数 backtrack(start, end)，它用于生成从 start 到 end 的所有排列。

初始状态：
nums = [1, 2, 3]
start = 0, end = 3 (因为数组长度为3)
res = [] （用于存储最终结果的空列表）
递归过程解释：
第一层递归 (start = 0):

循环 i 从 0 到 2。这意味着我们会尝试将 nums[0] 与 nums[i] 交换，其中 i 分别是 0, 1, 2。
当 i = 0 时，交换 nums[0] 和 nums[0]（实际上没有变化），然后递归调用 backtrack(1, 3)。
第二层递归 (start = 1):

现在，nums = [1, 2, 3]。
循环 i 从 1 到 2。
当 i = 1 时，交换 nums[1] 和 nums[1]（没有变化），递归调用 backtrack(2, 3)。
第三层递归 (start = 2):

现在，nums = [1, 2, 3]。
循环 i 从 2 到 2。
当 i = 2 时，交换 nums[2] 和 nums[2]（没有变化），递归调用 backtrack(3, 3)。
添加到结果列表:

在 backtrack(3, 3) 中，因为 start == end，所以我们将 nums[:] 添加到 res 中，此时 nums = [1, 2, 3]。
回溯并继续:

然后回溯到第二层递归，继续 i 的循环。例如，当 i = 2 时，交换 nums[1] 和 nums[2]，得到 nums = [1, 3, 2]，然后进入下一层递归。
这个过程会继续，直到所有可能的排列都被添加到 res 中。每当 start == end 时，意味着找到了一个完整的排列，它会被添加到结果列表中。
在每一次递归返回后，都会发生回溯，即将之前交换过的元素交换回原位置，以便进行下一次的排列尝试。

通过这种方式，算法能够遍历所有可能的排列，并将它们添加到结果列表中。
"""

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backtrack(start, end):
            # 如果到达数组末尾，添加排列到结果中
            if start == end:
                res.append(nums[:])
            for i in range(start, end):
                # 将nums[i]加入当前排列
                nums[start], nums[i] = nums[i], nums[start]
                # 继续递归填充下一个数
                backtrack(start + 1, end)
                # 回溯，撤销交换
                nums[start], nums[i] = nums[i], nums[start]

        res = []
        backtrack(0, len(nums))
        return res

