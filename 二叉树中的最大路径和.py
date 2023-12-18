"""
我们可以使用递归来遍历二叉树的每个节点。对于每个节点，我们考虑两种情况：
1. 通过该节点的最大路径和，这可能包括它的左右子树的一部分。
2. 该节点作为路径的一部分但不是根节点，这种情况下我们只能选择左子树或右子树的一条路径。
  我们需要一个辅助函数来计算每个节点作为根节点的最大路径和，同时更新全局的最大路径和。

下面是解决这个问题的步骤：
1. 定义一个全局变量 max_sum 用于存储遍历过程中找到的最大路径和。
2. 对于每个节点，我们计算通过该节点的最大单边路径和（即从该节点出发向下延伸到任何叶节点的最大路径和）。
  这个值等于该节点的值加上其左右子节点的最大单边路径和（如果这些单边路径和为正）。
3. 更新 max_sum，如果当前节点的值加上左右子节点的最大单边路径和大于 max_sum，则更新 max_sum。
4. 返回当前节点作为路径一部分的最大单边路径和，供上层节点使用
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 初始化最大路径和为负无穷
        self.max_sum = float("-inf")

        def max_gain(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # 递归计算左右子节点的最大单边路径和
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # 当前节点的最大路径和
            current_node_max = node.val + left_gain + right_gain
            
            # 更新全局最大路径和
            self.max_sum = max(self.max_sum, current_node_max)

            # 返回当前节点作为路径一部分的最大单边路径和
            return node.val + max(left_gain, right_gain)

        max_gain(root)

        return self.max_sum
