class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 如果总汽油小于总消耗，无法环绕一周
        if sum(gas) < sum(cost):
            return -1
        
        n = len(gas)
        total_tank, curr_tank = 0, 0
        starting_station = 0
        for i in range(n):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            # 如果当前油箱为空，则下一站成为新的起点
            if curr_tank < 0:
                starting_station = i + 1
                curr_tank = 0
        
        return starting_station if total_tank >= 0 else -1
