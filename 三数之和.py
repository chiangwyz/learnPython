"""
这个题目错了好几次，细节是魔鬼。
需要注意以下几个点：
1. third = length - 1 每次迭代都需要初始化
2. if second > first + 1 and nums[second] == nums[second-1]:  second > first + 1，因为second只需要对第二次出现的值进行比较，与第一次出现的值不需要比较
"""
class Solution:
    # [a, b, c]
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 返回值
        result = list()

        length = len(nums)

        # 对数组进行递增排序
        nums.sort()

        for first in range(length):
            if first > 0 and nums[first] == nums[first-1]:
                continue
            
            # 每次遍历的third都需要从后往前找
            third = length - 1

            # 需要匹配的数值
            target = - nums[first]

            for second in range(first + 1, length):
                if second > first + 1 and nums[second] == nums[second-1]:
                    continue
                
                # 在保证b的index小于c的index下，匹配target
                while second < third and nums[second] + nums[third] > target:
                    third -= 1

                if second >= third:
                    break

                if nums[second] + nums[third] == target:
                    result.append([nums[first], nums[second], nums[third]])
        
        return result



