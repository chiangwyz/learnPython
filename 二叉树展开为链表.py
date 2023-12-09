"""
要将给定的二叉树展开为单链表，我们可以利用二叉树的先序遍历（根-左-右）。
在展开的过程中，我们需要保持右子指针指向链表中的下一个节点，而左子指针始终为 null。我们可以通过递归或迭代的方式来实现这个过程。

下面是一个使用递归方法的解题思路：

基本情况: 如果根节点是 null，就直接返回，因为没有什么可以展开的。

递归展开: 我们先递归地展开左子树和右子树。

重构树结构: 展开后，我们首先将根节点的右子树指向根节点的左子树的最右边的节点，然后将根节点的左子树设置为 null，并将原来的右子树接到当前右子树的末端。

更新右子节点: 最后，将根节点的右子节点更新为原来左子节点的根。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        # 先序递归展开左右子树
        self.flatten(root.left)
        self.flatten(root.right)

        # 保存右子树
        temp_right = root.right

        # 将左子树移到右子树位置
        root.right = root.left
        root.left = None  # 左子树置为 null

        # 找到当前右子树的末端
        while root.right:
            root = root.right

        # 将保存的原右子树接到当前右子树末端
        root.right = temp_right
