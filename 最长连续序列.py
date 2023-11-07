"""
首先通过将数组转换为集合来消除重复的元素，并允许 O(1) 时间复杂度的成员检查。然后，它只尝试在集合中找到序列的开始（通过检查 num - 1 是否存在），从而避免重复计算已经找到的序列。对于每个序列的开始，它计算序列的长度，并更新最长序列的长度。这样保证了整个算法的时间复杂度为 O(n)，因为每个数字最多只被访问两次：一次是在将 nums 转换为集合时，一次是在找到序列开始时。
"""
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # 创建一个包含所有元素的集合，用于O(1)的查找
        nums_set = set(nums)
        longest_streak = 0
        current_streak = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in nums_set:
                    current_streak += 1
                    current_num += 1

                # 更新最长连续序列的长度
                longest_streak = max(longest_streak, current_streak)

        return longest_streak



