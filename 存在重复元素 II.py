class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        index_map = {}  # 存储元素及其最近出现的索引

        for i, num in enumerate(nums):
            if num in index_map and i - index_map[num] <= k:
                return True  # 发现重复元素，且它们的索引差不大于 k
            index_map[num] = i  # 更新元素的最新索引

        return False  # 遍历完数组后没有找到满足条件的元素对

# 示例测试
sol = Solution()
print(sol.containsNearbyDuplicate([1,2,3,1], 3))  # 输出：True
print(sol.containsNearbyDuplicate([1,0,1,1], 1))  # 输出：True
print(sol.containsNearbyDuplicate([1,2,3,1,2,3], 2))  # 输出：False
