"""
为了检查一个二叉树是否轴对称，我们可以使用递归的方法。
基本思路是比较树的左子树和右子树是否是镜像对称的。
对于两个子树来说，要满足以下条件才能认为它们是对称的：

两个子树的根节点的值相同。
左子树的左子节点和右子树的右子节点对称（它们的值相同，且子树结构对称）。
左子树的右子节点和右子树的左子节点对称。
"""

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True  # 空树被视为对称的
        
        return self.isMirror(root.left, root.right)  # 检查左右子树是否为镜像

    def isMirror(self, left: TreeNode, right: TreeNode) -> bool:
        if not left and not right:
            return True  # 两个空节点视为对称
        if not left or not right:
            return False  # 一个节点为空，另一个不为空，不对称
        if left.val != right.val:
            return False  # 两个节点的值不同，不对称

        # 递归检查当前节点的左右子节点是否为镜像
        return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
