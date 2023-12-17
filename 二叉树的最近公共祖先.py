"""
为了找到给定二叉树中两个指定节点的最近公共祖先，我们可以使用递归方法。
这个问题的关键是向下遍历树，直到找到两个节点或达到叶节点。递归函数将检查当前节点是否是其中一个目标节点（p 或 q），如果是，则返回当前节点。

递归的基本思路如下：

如果当前节点为 null，返回 null。
如果当前节点等于 p 或 q 中的任何一个，返回当前节点。
对当前节点的左右子树分别调用递归函数。
如果左右子树的递归调用都返回非 null 值，意味着找到了 p 和 q 的最近公共祖先，返回当前节点。
如果只有一个子树的递归调用返回非 null 值，则最近公共祖先在那个子树中。
如果两个子树的递归调用都返回 null，则最近公共祖先不存在于这两个子树中。

"""


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 如果到达了叶节点（root 为 None），或者找到了 p 或 q 中的任意一个，返回当前节点
        if root is None or root == p or root == q:
            return root

        # 对当前节点的左子树进行递归搜索
        left = self.lowestCommonAncestor(root.left, p, q)
        # 对当前节点的右子树进行递归搜索
        right = self.lowestCommonAncestor(root.right, p, q)

        # 如果左右子树的递归调用都返回了非空节点（即找到了 p 和 q），则当前节点是它们的最近公共祖先
        if left is not None and right is not None:
            return root

        # 如果只有一个子树的递归调用返回了非空节点，则最近公共祖先在那个子树中
        # 如果 left 不为空，则返回 left，否则返回 right
        return left if left is not None else right
