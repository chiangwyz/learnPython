"""
这个算法的核心在于遍历数组的同时，不断更新在当前位置所能到达的最远距离。如果在某个点，这个最远距离小于当前索引，说明你无法越过这个点。如果最远距离大于或等于数组的最后一个下标，说明你能到达数组的末尾。
要注意for循环内部的三段代码的执行的先后顺序。

"""
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # 最远可以到达的距离
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:
                return False

            max_reach = max(max_reach, i+nums[i])

            if max_reach >= len(nums)-1:
                return True
            
        return False
