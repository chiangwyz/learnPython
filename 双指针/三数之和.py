"""
这个题目错了好几次，细节是魔鬼。

在这个问题中，要求找出所有不重复的三元组，其元素之和为0。
如果在数组中连续的两个数相同，那么这两个数会产生相同的三元组，因为它们与数组中的其他数结合时，除了它们自身的位置不同之外，其他元素和结果都会相同。
这就违反了问题中的“答案中不可以包含重复的三元组”的要求。

例如，如果数组排序后为 [-1, -1, 0, 1, 2]，第一个 -1 和第二个 -1 都可以与 [0, 1] 组合成 [-1, 0, 1]，但我们只需要记录这个组合一次。

因此，当遇到连续相同的数字时，我们只需考虑第一次出现的数字，后续相同的数字可以跳过。这样做的目的是为了避免在结果集中出现重复的三元组。
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 返回的数组
        result = []
        # 首先对数组进行排序
        nums.sort()
        # 获取数组长度
        n = len(nums)

        # 遍历每个数
        for i in range(n):
            # 跳过重复的数
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # 使用双指针
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    # 找到了一个解
                    result.append([nums[i], nums[left], nums[right]])
                    # 第二个数、第三个数也要跳过重复的数
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # 更新左右指针
                    left += 1
                    right -= 1
        
        return result

# 示例测试
sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))  # 输出：[[-1, -1, 2], [-1, 0, 1]]
print(sol.threeSum([0, 1, 1]))  # 输出：[]
print(sol.threeSum([0, 0, 0]))  # 输出：[[0, 0, 0]]





