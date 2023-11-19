"""
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
"""

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0  # 初始化计数器
        candidate = None  # 初始化候选多数元素为None

        # 遍历每个元素
        for num in nums:
            # 如果计数器为0，选择当前元素作为新的候选多数元素
            if count == 0:
                candidate = num
                count = 1
            else:
                # 如果当前元素等于候选多数元素，计数器加一
                if num == candidate:
                    count += 1
                # 如果当前元素不等于候选多数元素，计数器减一
                else:
                    count -= 1

        # 返回候选多数元素
        return candidate







