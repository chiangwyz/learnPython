"""
使用一个指针insertPos来指示下一个非零元素应该插入的位置。
遍历数组，每当遇到非零元素时，就将其移动到insertPos的位置，并将insertPos向前移动一位。
遍历结束后，insertPos及其之后的所有位置都应该填充0。
"""
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insertPos = 0

        for num in nums:
            if num != 0:
                nums[insertPos] = num
                insertPos += 1

        while insertPos < len(nums):
            nums[insertPos] = 0
            insertPos += 1
