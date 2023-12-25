"""
示例 1：
输入：nums = [1,1,2]
输出：2, nums = [1,2,_]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。

示例 2：
输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。
"""
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
