class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []

        ranges = []
        start = end = nums[0]

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
                start = end = n

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




