"""
该题目简单，主要考察对数组的基本理解。
"""
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # 初始化一个新的index
        nex_index = 0

        # 遍历数组，只要当前元素不等于val，则重新赋值，只要等于val，则略过
        for i in range(len(nums)):
            if nums[i] != val:
                nums[nex_index] = nums[i]
                nex_index += 1
        
        # 返回的nex_index即为数组长度
        return nex_index
