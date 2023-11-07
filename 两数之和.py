"""
假设给定列表 [2,5,7,11]，目标值为9，
该思路还是蛮有趣的，通过num_dict存储7需要的2的index，即num_dict[7] = 0
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Create a dictionary to store the difference between the target and the nums value
        num_dict = {}
        # Enumerate through the nums array
        for i, num in enumerate(nums):
            # If num exists in the dictionary, we have found the pair
            if num in num_dict:
                return [num_dict[num], i]
            # Otherwise, store the index of the required pair element
            else:
                num_dict[target - num] = i
