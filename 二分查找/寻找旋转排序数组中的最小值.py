"""
1. 初始化两个指针，left 和 right，分别指向数组的起始位置和结束位置。
2. 找到数组的中间位置 mid。
3. 比较 mid 位置的元素和 right 位置的元素：
    如果 mid 位置的元素小于 right 位置的元素，这意味着 mid 到 right 这部分是有序的。
    因此，最小元素可能是 mid 位置的元素，或者在 left 到 mid 这部分。
    如果 mid 位置的元素大于 right 位置的元素，这意味着 left 到 mid 这部分是有序的，
    且最小元素在 mid 到 right 这部分。
4. 通过以上判断，调整 left 或 right 指针，缩小查找范围。
5. 重复上述过程，直到 left 和 right 相遇，此时找到的元素即为最小元素。
"""


class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right + left) // 2
            # 如果中间元素小于最右边的元素，最小值在左半部分
            if nums[mid] < nums[right]:
                right = mid
            else:
                # 否则最小值在右半部分
                left = mid + 1
        # 当left等于right时，找到最小值
        return nums[left]


# test
sol = Solution()
print(sol.findMin([3, 4, 5, 1, 2]))  # 输出: 1
print(sol.findMin([4, 5, 6, 7, 0, 1, 2]))  # 输出: 0
print(sol.findMin([11, 13, 15, 17]))  # 输出: 11
