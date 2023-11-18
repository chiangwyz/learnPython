class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # 初始化新的索引为1，因为至少有一个唯一的元素
        new_index = 1

        # 遍历数组中的每个元素，从索引1开始，因为第一个元素总是唯一的
        for i in range(1, len(nums)):
            # 如果当前元素与新索引前一个元素不同，则它是唯一的
            if nums[i] != nums[new_index - 1]:
                # 将其移动到新索引的位置
                nums[new_index] = nums[i]
                # 新索引后移
                new_index += 1

        # 返回新的数组长度，也就是唯一元素的个数
        return new_index
