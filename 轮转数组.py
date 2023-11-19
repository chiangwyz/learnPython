class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 由于轮转k次和轮转n次效果相同，其中n是数组长度，我们使用k对数组长度取模
        k = k % len(nums)
        # 首先，将整个数组翻转
        nums.reverse()
        # 然后，翻转前k个元素
        nums[:k] = reversed(nums[:k])
        # 最后，翻转剩下的元素
        nums[k:] = reversed(nums[k:])
