"""
为了解决这个问题，我们可以使用深度优先搜索（DFS）算法。
深度优先搜索是一种用于遍历或搜索树或图的算法。
这种方法沿着树的深度遍历树的节点，尽可能深地搜索树的分支。

对于这个问题，我们将从根节点开始，然后递归地遍历每个子节点。
对于每个节点，我们需要维护一个当前的数字值，这个值等于从根节点到当前节点路径上形成的数字。
当我们到达一个叶节点时，我们将其值添加到总和中。

以下是解决这个问题的步骤：
1. 从根节点开始。
2. 对于每个节点，计算到当前节点为止形成的数字。
3. 如果当前节点是叶节点，将其值加到总和中。
4. 递归地遍历当前节点的左右子节点。
5. 返回总和。
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_number):
            # 如果当前节点为空，返回0
            if not node:
                return 0

            # 更新到当前节点为止形成的数字
            current_number = current_number * 10 + node.val

            # 如果是叶节点，返回当前形成的数字
            if not node.left and not node.right:
                return current_number

            # 递归遍历左子节点和右子节点，并返回它们的和
            return dfs(node.left, current_number) + dfs(node.right, current_number)

        # 从根节点开始深度优先搜索
        return dfs(root, 0)
