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
