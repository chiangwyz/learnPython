"""
给定一个  无重复元素 的 有序 整数数组 nums 。
返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表 。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，
并且不存在属于某个范围但不属于 nums 的数字 x 。

列表中的每个区间范围 [a,b] 应该按如下格式输出：
"a->b" ，如果 a != b
"a" ，如果 a == b

示例 1：
输入：nums = [0,1,2,4,5,7]
输出：["0->2","4->5","7"]
解释：区间范围是：
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
"""
class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []

        ranges = []
        start = nums[0]
        end = nums[0]

        for n in nums[1:]:
            # 如果当前数字与前一个数字连续，则更新区间的结束数字
            if n == end + 1:
                end = n
            else:
                # 如果当前数字与前一个数字不连续，结束当前区间，并开始一个新区间
                if start == end:
                    ranges.append(str(start))
                else:
                    ranges.append("{}->{}".format(start, end))

                # 更新起始区间
                start = n
                end = n

        # 添加最后一个区间
        if start == end:
            ranges.append(str(start))
        else:
            ranges.append("{}->{}".format(start, end))

        return ranges

# 示例测试
sol = Solution()
print(sol.summaryRanges([0,1,2,4,5,7]))  # 输出：["0->2","4->5","7"]
print(sol.summaryRanges([0,2,3,4,6,8,9]))  # 输出：["0","2->4","6","8->9"]




