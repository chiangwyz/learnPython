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
