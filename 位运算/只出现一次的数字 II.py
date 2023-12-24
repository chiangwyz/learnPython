"""
该题目有两种解法，一种是位解法，另一种是哈希算法。

哈希解法
1. 创建一个哈希表（在Python中通常使用字典）来存储每个元素出现的次数。
2. 遍历数组，更新哈希表中每个元素的出现次数。
3. 再次遍历哈希表，找到那个出现次数为1的元素并返回。
这种方法的时间复杂度是O(n)，因为我们需要遍历两次数组（一次是数组本身，一次是哈希表）。
但空间复杂度是O(n)，因为我们使用了额外的哈希表来存储元素和它们的出现次数。

"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}  # 初始化哈希表

        # 遍历数组，更新哈希表中的元素出现次数
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # 遍历哈希表，找到只出现一次的元素
        for num in count:
            if count[num] == 1:
                return num
