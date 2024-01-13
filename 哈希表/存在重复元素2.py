class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # 存储元素及其最近出现的索引
        index_map = {}

        for index, num in enumerate(nums):
            if num in index_map and index - index_map[num] <= k:
                # 发现重复元素，且它们的索引差不大于 k
                return True
                # 更新元素的最新索引
            index_map[num] = index
        # 遍历完数组后没有找到满足条件的元素对
        return False


# 示例测试
sol = Solution()
print(sol.containsNearbyDuplicate([1, 2, 3, 1], 3))  # 输出：True
print(sol.containsNearbyDuplicate([1, 0, 1, 1], 1))  # 输出：True
print(sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  # 输出：False
