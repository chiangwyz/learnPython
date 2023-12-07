"""
要解决这个问题，首先要理解先序遍历和中序遍历在二叉树中的角色。
在先序遍历中，我们首先访问根节点，然后是左子树，最后是右子树。
在中序遍历中，我们首先访问左子树，然后是根节点，最后是右子树。

这个问题的关键在于利用这两种遍历的特点来重建二叉树。
首先，先序遍历的第一个元素是树的根节点。我们可以利用这个根节点将中序遍历分为两部分：左子树和右子树。
接着，我们可以对先序遍历和中序遍历的左右子树分别递归地应用同样的方法，来构建整棵树。

以下是实现这个算法的步骤：

1如果先序遍历数组为空，返回空。
2先序遍历的第一个元素是根节点。创建这个根节点。
3在中序遍历数组中找到根节点的位置，这将数组分为左子树和右子树两部分。
4递归地在左子树的先序遍历和中序遍历上重建左子树。
5递归地在右子树的先序遍历和中序遍历上重建右子树。
6返回根节点。
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # 先序遍历的第一个值就是根节点
        root = TreeNode(preorder[0])
        # 在中序遍历中找到根节点的位置
        mid = inorder.index(preorder[0])

        # 递归构造左子树和右子树
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
