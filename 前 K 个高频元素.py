class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 统计每个元素出现的次数
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        
        # 准备返回结果的列表
        res = []
        # 执行 k 次，每次找出一个出现频率最高的元素
        while k > 0:
            # 初始化临时变量，用于记录当前找到的最大频率
            tmp = 0
            # 初始化变量 cur，用于记录当前频率最高的元素
            cur = nums[0]
            # 遍历字典，找到出现频率最高的元素
            for num in dic:
                if dic[num] > tmp:
                    tmp = dic[num]
                    cur = num
            # 将当前频率最高的元素计数设置为 -1，这样它就不会在下一次循环中被选中
            dic[cur] = -1
            # 将当前频率最高的元素添加到结果列表中
            res.append(cur)
            # 减少 k 的值，因为我们已经找到了一个频率最高的元素
            k -= 1
        # 返回结果列表
        return res
