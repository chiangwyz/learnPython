"""
思路说明
翻转二叉树的基本思路是将每个节点的左右子树进行交换。
这个过程可以通过递归实现。对于每个节点，我们做以下操作：

如果当前节点为空（比如，叶子节点的子节点），则直接返回，不进行任何操作。
交换当前节点的左右子节点。
递归地对左子树和右子树执行相同的翻转操作。
这个过程从根节点开始，并遍历整个树，确保每个节点的左右子树都被交换。
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 当前节点为空时直接返回
        if not root:
            return None

        # 交换当前节点的左右子节点
        root.left, root.right = root.right, root.left

        # 递归翻转左右子树
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
