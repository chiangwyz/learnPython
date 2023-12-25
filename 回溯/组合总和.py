"""
要解决这个问题，可以使用回溯算法。需要不断尝试添加不同的数字，直到总和达到目标值或超过目标值。
如果总和等于目标值，我们就找到了一个有效的组合。如果总和超过目标值，我们就回溯到上一步，尝试其他的数字。

以下是解决这个问题的步骤和代码：

1. 创建一个辅助函数来进行回溯。
2. 在辅助函数中，遍历数组中的每个数字。
3. 对每个数字，我们有两个选择：要么将其加入当前组合，要么不加入。
4. 如果当前总和加上这个数字仍然小于或等于目标值，我们将其加入当前组合，并继续递归。
5. 如果当前总和加上这个数字大于目标值，我们停止递归。
6. 当总和等于目标值时，将当前组合加入到结果列表中。
7. 最终返回所有可能的组合。
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path):
            # 如果目标值为0，则找到了一个有效的组合
            if target == 0:
                result.append(path.copy())
                return
            # 遍历所有可能的选择
            for i in range(start, len(candidates)):
                # 如果当前值小于或等于目标值，则尝试添加它
                if candidates[i] <= target:
                    path.append(candidates[i])
                    # 继续探索，注意我们不增加索引值，因为我们可以重复使用相同的数字
                    backtrack(i, target - candidates[i], path)
                    # 回溯，移除最后一个元素，尝试下一个选择
                    path.pop()

        result = []
        backtrack(0, target, [])
        return result


