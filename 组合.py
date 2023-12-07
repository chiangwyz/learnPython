"""
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
你可以按 任何顺序 返回答案。

示例 1：
输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

示例 2：
输入：n = 1, k = 1
输出：[[1]]

详细解释这个问题的解决方案。这个问题是关于如何生成从 1 到 n 的所有可能的 k 个数的组合。我们使用了回溯算法来解决这个问题，下面是具体的解题思路：

解题思路
初始化结果列表:
创建一个空列表 result，用于存储所有合法的组合。

定义回溯函数:
回溯函数 backtrack(start, path) 接收两个参数：

start: 表示开始的数字，用于确保组合中的数字是升序排列的，避免重复。
path: 当前构建的组合。
处理终止条件:
当 path 的长度等于 k 时，意味着我们找到了一个合法的组合。我们将其添加到 result 中并返回。这是回溯搜索的终止条件。

递归和回溯:
在每一层的递归中，我们从 start 到 n 遍历每一个数字：

对于每个数字 i，我们将它添加到 path 中，并递归调用 backtrack(i + 1, path)。这里 i + 1 作为下一步的起始数字，确保了数字的升序排列。
完成递归调用后，我们需要“回溯”，即移除 path 中最后添加的数字，以便于尝试其他可能的数字。
开始回溯:
使用 backtrack(1, []) 开始回溯过程，从数字 1 开始尝试所有可能的组合。

示例分析
举例来说，对于 n = 4 和 k = 2 的情况：

回溯开始时，path 是空的。
首先，数字 1 被添加到 path，然后探索所有包含 1 的组合。
接着，数字 2 被添加，形成 [1, 2]，由于这是一个有效的组合，它被添加到结果中。
然后，回溯将 2 从 path 中移除，并尝试 3 和 4，形成 [1, 3] 和 [1, 4]。
同样的过程也会应用于开始于 2、3 和 4 的其他组合。
结果
这个方法有效地枚举了从 1 到 n 的所有可能的 k 个数的组合，确保了每个组合都是独一无二的，并按照升序排列。通过这种方式，我们能够找到并返回所有可能的组合。
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, path):
            # 如果路径的长度等于 k，加入到结果中
            if len(path) == k:
                result.append(path.copy())
                return
            
            # 从 start 到 n 遍历
            for i in range(start, n + 1):
                # 添加当前数到路径，并继续下一步
                path.append(i)
                backtrack(i + 1, path)
                # 回溯，移除路径中最后一个数
                path.pop()

        result = []
        backtrack(1, [])
        return result

# 测试代码
sol = Solution()
example1 = sol.combine(4, 2)
example2 = sol.combine(1, 1)

example1, example2
