"""
为了计算二叉树的最大深度，我们可以使用递归的方法。
基本思想是比较左子树和右子树的深度，取其中较大的一个，
并加上当前节点自身的深度。这里是相应的实现代码和注释：

这个方法遵循了分治法的思想，即将问题分解为子问题，
分别解决后再将结果合并。对于每一个节点，
它的深度等于其左右子节点的最大深度加1。
递归的终止条件是当遇到空节点时返回0，因为空节点不增加树的深度。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 如果节点为空，深度为0
        if root is None:
            return 0

        # 递归计算左子树的深度
        left_depth = self.maxDepth(root.left)
        # 递归计算右子树的深度
        right_depth = self.maxDepth(root.right)

        # 当前节点的最大深度是左右子树深度的最大值加1（加的1是当前节点本身的深度）
        return max(left_depth, right_depth) + 1
