"""
在一个完全二叉树中，我们可以观察到以下特性：

如果一棵树的左子树和右子树的高度相同，那么这棵树的左子树一定是一个满二叉树。
这是因为在完全二叉树中，除了最底层，其他每层都是满的，而最底层的节点是从左到右填充的。
所以，如果左右子树高度相同，意味着最底层左子树是完全填充的，而右子树的最底层可能没有完全填充。

如果左子树的高度大于右子树的高度，那么右子树是一个满二叉树。
这是因为在完全二叉树中，最底层的节点填充是从左到右的，所以如果左子树比右子树高，
说明左子树的最底层没有完全填充，而右子树的每一层都已经填满了。

解题思路：

1. 我们首先需要定义一个函数来计算树的高度，这里的高度是指从根节点到最左侧叶子节点的路径长度。
2. 接着，我们对根节点进行判断。如果根节点为空，则树没有节点，返回0。
3. 我们计算左子树和右子树的高度。如果左子树的高度等于右子树的高度，说明左子树是一个完全二叉树，
  我们可以直接根据高度计算出左子树的节点数，然后递归计算右子树的节点数。
  如果左子树高度大于右子树高度，说明最后一层的节点没有完全填满，
  我们可以直接计算右子树的节点数（因为右子树是一个高度比左子树小一的完全二叉树），然后递归计算左子树的节点数。
4. 最后，将得到的节点数相加，再加上根节点本身，就是整棵树的节点总数。
"""

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def treeHeight(node):
            # 计算树的高度
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        if not root:
            # 如果根节点为空，返回0
            return 0

        left_height = treeHeight(root.left)
        right_height = treeHeight(root.right)

        if left_height == right_height:
            # 如果左子树和右子树高度相同，说明左子树是完全二叉树
            return (2 ** left_height) + self.countNodes(root.right)
        else:
            # 如果左子树高度大于右子树，说明右子树是完全二叉树
            return (2 ** right_height) + self.countNodes(root.left)

# 示例使用
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)
# solution = Solution()
# print(solution.countNodes(root))  # 输出: 6
