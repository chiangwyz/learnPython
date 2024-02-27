"""
解题思路：
1. 首先，我们检查是否有解：如果总的 gas 小于总的 cost，那么没有足够的油可以环绕一周，直接返回 -1。
2. 然后，我们遍历加油站数组。我们维护两个变量：total_tank 来追踪总油量，和 curr_tank 来追踪从当前起始加油站出发的油量。
    如果在某个点 curr_tank 降到了小于 0，这意味着从当前起始加油站无法到达这个点，所以我们需要更新起始加油站为当前点的下一站，并将 curr_tank 重置为 0。
3. 每当我们更新起始加油站，我们不需要重置 total_tank，因为它是用来追踪总的油量是否足够。
4. 遍历结束后，如果 total_tank 仍然大于等于 0，那么起始加油站就是我们的答案，否则返回 -1

关键点
为什么选择下一个加油站作为新的起点:
当 curr_tank 变为负数时，意味着从 starting_station 到当前加油站的任何一个加油站都不能作为有效的起点。
因为如果在这些加油站之间的任何一个开始，到达当前加油站时，汽油量肯定会小于0。
因此，只能选择当前加油站的下一个加油站作为新的起点。

总体思路:
这个算法的关键在于逐步排除那些无法作为有效起始点的加油站，并在确认总油量足以完成整个旅程后，找到一个有效的起始点。
这是一种贪心算法的实现，它在每一步都做出当时看起来最好的选择（即选择下一个加油站作为新的起始点），最终得到全局最优解。
"""
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        # 如果总汽油小于总消耗，无法环绕一周
        if sum(gas) < sum(cost):
            return -1

        # 加油站的数量
        n = len(gas)  
        # 总油量，用于计算总油量是否大于总耗油量
        total_tank = 0  
        # 当前油量，用于计算从某个加油站出发是否能到达下一个加油站
        curr_tank = 0  
        # 起始加油站的索引
        starting_station = 0  
    
        # 遍历每个加油站
        for i in range(n):
            # 更新总油箱和当前油箱的油量
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            
            # 如果当前油箱为空，则不能从当前加油站到达下一个加油站
            # 因此需要从下一个加油站重新开始计算
            if curr_tank < 0:
                # 更新起始加油站为下一个加油站
                starting_station = i + 1  
                # 重置当前油箱为空
                curr_tank = 0 
    
        # 如果总油箱中的油足以走完全程，返回有效的起始加油站
        if total_tank >= 0:
            return starting_station
        else:
            return -1


import unittest


class TestGasStation(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_can_complete_circuit(self):
        # 测试可以环绕一周的情况
        self.assertEqual(self.solution.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3)

    def test_cannot_complete_circuit(self):
        # 测试无法环绕一周的情况
        self.assertEqual(self.solution.canCompleteCircuit([2, 3, 4], [3, 4, 3]), -1)

    def test_total_gas_equals_total_cost(self):
        # 测试总油量正好等于总消耗量的情况
        self.assertEqual(self.solution.canCompleteCircuit([2, 3, 1], [3, 1, 2]), 1)

    def test_single_station(self):
        # 测试只有一个加油站的情况
        self.assertEqual(self.solution.canCompleteCircuit([1], [1]), 0)
        self.assertEqual(self.solution.canCompleteCircuit([2], [3]), -1)

    def test_no_valid_start(self):
        # 测试多个加油站但无法找到起点的情况
        self.assertEqual(self.solution.canCompleteCircuit([1, 2, 3, 4, 5], [5, 5, 5, 5, 5]), -1)


if __name__ == '__main__':
    unittest.main()
