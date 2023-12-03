"""
这个方法的核心在于递归地比较两棵树的节点。
首先，我们检查两棵树的根节点是否都为空，如果是，则树相同。
其次，如果其中一个树的根节点为空而另一个不是，这两棵树不相同。
接着，如果两棵树的根节点的值不同，那么树也不相同。
最后，如果根节点的值相同，我们递归地比较左子树和右子树。
只有在所有对应的左子树和右子树都相同的情况下，这两棵树才被认为是相同的。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 如果两个树都是空的，则它们是相同的
        if not p and not q:
            return True

        # 如果其中一个树是空的，另一个不是，则它们不相同
        if not p or not q:
            return False

        # 如果两个树的根节点的值不同，则它们不相同
        if p.val != q.val:
            return False

        # 递归地检查左子树和右子树
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

