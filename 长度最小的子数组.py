class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        sum = 0
        # 使用无穷大初始化最小长度
        min_length = float('inf')  

        # 遍历数组
        for right in range(n):
            # 累加子数组的和
            sum += nums[right]
            # 当和大于等于target时，尝试缩小子数组的长度
            while sum >= target:
                # 更新最小长度
                min_length = min(min_length, right - left + 1)
                # 移动左指针，减小子数组的和
                sum -= nums[left]  
                left += 1
        
        # 如果min_length没有被更新过，说明没有找到符合条件的子数组
        return 0 if min_length == float('inf') else min_length

# 示例测试
sol = Solution()
print(sol.minSubArrayLen(7, [2,3,1,2,4,3]))  # 输出：2
print(sol.minSubArrayLen(4, [1,4,4]))  # 输出：1
print(sol.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))  # 输出：0

