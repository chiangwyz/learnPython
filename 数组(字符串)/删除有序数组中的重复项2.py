class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 数组长度小于3，不可能有超过两次的重复
        if len(nums) < 3:
            return len(nums)

        # 新索引从2开始，因为前两个元素允许重复
        new_index = 2

        # 从第三个元素开始遍历
        for i in range(2, len(nums)):
            # 如果当前元素不等于新索引位置前两个元素的值，则它是允许的第二个重复
            if nums[i] != nums[new_index - 2]:
                nums[new_index] = nums[i]
                new_index += 1

        return new_index
