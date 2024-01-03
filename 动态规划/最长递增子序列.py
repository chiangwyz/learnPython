"""
定义一个数组 dp，其中 dp[i] 表示以 nums[i] 结尾的最长递增子序列的长度。

1. 初始化 dp 数组，所有元素都设置为 1，因为最短的递增子序列至少包含一个元素。
2. 对于 nums 中的每个元素，我们遍历它之前的所有元素。
  如果当前元素 nums[i] 大于之前的某个元素 nums[j]，这意味着我们可以将 nums[i] 添加到以 nums[j] 结尾的递增子序列中。
  我们更新 dp[i] 为 dp[j] + 1 和当前的 dp[i] 中的较大值。
3. 遍历完成后，dp 数组中的最大值即为整个数组的最长递增子序列的长度。
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # 初始化dp数组，每个元素的初始值为1，因为最短的递增子序列包含它自己
        dp = [1] * len(nums)

        # 遍历数组中的每个元素
        for i in range(1, len(nums)):
            # 再遍历当前元素之前的所有元素
            for j in range(i):
                # 如果当前元素大于之前的某个元素
                if nums[i] > nums[j]:
                    # 更新dp[i]，使其等于dp[j] + 1和当前dp[i]的较大者
                    dp[i] = max(dp[i], dp[j] + 1)

        # 返回dp数组中的最大值，即为最长递增子序列的长度
        return max(dp)





