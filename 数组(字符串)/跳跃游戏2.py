"""
代码中的循环不包含数组的最后一个元素，是因为题目假设了总是可以到达数组的最后一个位置。
这意味着在数组中不会存在这样的情况，即你被困在某个位置无法到达数组的末尾。换句话说，题目保证了至少有一条路径可以从数组的开始跳到结尾。

变量初始化:
jumps: 记录跳跃的次数。
current_end: 记录当前跳跃能到达的最远位置。
farest: 记录在当前步骤及之前所有步骤中，能跳到的最远位置。

1. 循环遍历数组 (for i in range(len(nums) - 1)):
2. 这个循环不包括数组的最后一个元素，因为当到达或超过最后一个元素时，就不需要再跳跃了。
3. 在每一步中，更新farest为当前位置加上该位置能跳的最大长度（i + nums[i]）和之前的farest中的较大值。
4. 判断是否需要进行新的跳跃 (if i == current_end):
    当i达到current_end时，意味着已经达到了上一次跳跃能到达的最远位置。
5. 这时需要进行新的跳跃，因此将jumps增加1。
6. 同时，更新current_end为farest，即新的跳跃能到达的最远位置。
7. 返回跳跃次数 (return jumps):

循环结束后，jumps中存储的就是到达数组末尾所需的最小跳跃次数。
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
