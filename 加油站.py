"""
在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。
给定两个整数数组 gas 和 cost ，如果你可以按顺序绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1 。如果存在解，则 保证 它是 唯一 的。

1. 首先判断总gas能不能大于等于总cost，如果总gas不够，一切都白搭对吧（总（gas- cost）不用单独去计算，和找最低点时一起计算即可，只遍历一次）；
2. 再就是找总（gas-cost）的最低点，不管正负（当然如果最低点都是正的话那肯定能跑完了）；
3. 找到最低点后，如果有解，那么解就是最低点的下一个点，因为总（gas-cost）是大于等于0的，所以前面损失的gas我从最低点下一个点开始都会拿回来！
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 总油量小于总消耗，无法完成环绕
        if sum(gas) < sum(cost):
            return -1
        
        n = len(gas)
        total_tank, curr_tank = 0, 0
        starting_station = 0
        for i in range(n):
            total_tank += gas[i] - cost[i]  # 总油量与总消耗的差
            curr_tank += gas[i] - cost[i]   # 当前油箱油量
            # 如果当前油箱油量小于0，下一个加油站成为新的起点
            if curr_tank < 0:
                starting_station = i + 1
                curr_tank = 0
        
        # 如果总油量大于等于总消耗，返回起始加油站；否则返回-1
        return starting_station if total_tank >= 0 else -1
