"""
在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。
给定两个整数数组 gas 和 cost ，如果你可以按顺序绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1 。如果存在解，则 保证 它是 唯一 的。

解题思路：
1. 首先，我们检查是否有解：如果总的 gas 小于总的 cost，那么没有足够的油可以环绕一周，直接返回 -1。
2. 然后，我们遍历加油站数组。我们维护两个变量：total_tank 来追踪总油量，和 curr_tank 来追踪从当前起始加油站出发的油量。如果在某个点 curr_tank 降到了小于 0，这意味着从当前起始加油站无法到达这个点，所以我们需要更新起始加油站为当前点的下一站，并将 curr_tank 重置为 0。
3. 每当我们更新起始加油站，我们不需要重置 total_tank，因为它是用来追踪总的油量是否足够。
4. 遍历结束后，如果 total_tank 仍然大于等于 0，那么起始加油站就是我们的答案，否则返回 -1
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 如果总汽油小于总消耗，无法环绕一周
        if sum(gas) < sum(cost):
            return -1
        
        n = len(gas)  # 加油站的数量
        total_tank = 0  # 总油箱，用于计算总油量是否大于总耗油量
        curr_tank = 0  # 当前油箱，用于计算从某个加油站出发是否能到达下一个加油站
        starting_station = 0  # 起始加油站的索引
    
        # 遍历每个加油站
        for i in range(n):
            # 更新总油箱和当前油箱的油量
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            
            # 如果当前油箱为空，则不能从当前加油站到达下一个加油站
            # 因此需要从下一个加油站重新开始计算
            if curr_tank < 0:
                starting_station = i + 1  # 更新起始加油站为下一个加油站
                curr_tank = 0  # 重置当前油箱为空
    
        # 如果总油箱的油量大于等于0，则可以环绕一周，返回起始加油站索引
        # 否则，返回-1表示无法环绕一周
        return starting_station if total_tank >= 0 else -1
