"""
给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。
每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:
0 <= j <= nums[i] 
i + j < n
返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0
        
        # 遍历到倒数第二个元素，因为开始时不需要跳跃，而且最后一个元素是目的地
        for i in range(len(nums) - 1):
            # 找到能跳到的最远的地方
            farthest = max(farthest, i + nums[i])
            # 如果到达了当前跳跃能到的边界
            if i == current_end:
                # 进行跳跃
                jumps += 1
                # 更新当前跳跃能到达的边界
                current_end = farthest
        
        return jumps
