"""
该题目简单，主要考察对数组的基本理解。

示例 1：
输入：nums = [3,2,2,3], val = 3
输出：2, nums = [2,2]
解释：函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
你不需要考虑数组中超出新长度后面的元素。例如，函数返回的新长度为 2 ，而 nums = [2,2,3,3] 或 nums = [2,2,0,0]，也会被视作正确答案。

示例 2：
输入：nums = [0,1,2,2,3,0,4,2], val = 2
输出：5, nums = [0,1,3,0,4]
解释：函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。注意这五个元素可为任意顺序。你不需要考虑数组中超出新长度后面的元素。
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 初始化一个新的index
        nex_index = 0

        # 遍历数组，只要当前元素不等于val，则重新赋值，只要等于val，则略过
        for i in range(len(nums)):
            if nums[i] != val:
                nums[nex_index] = nums[i]
                nex_index += 1
        
        # 返回的nex_index即为数组长度
        return nex_index
