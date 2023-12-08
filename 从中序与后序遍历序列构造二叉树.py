"""
这个问题的解决方案基于二叉树的中序遍历（inorder）和后序遍历（postorder）来重建二叉树。以下是详细的解题思路，以及代码的中文注释。

解题思路：

1 在后序遍历中，最后一个元素总是树的根节点。
2 在中序遍历中找到根节点的位置，这将数组分为左子树和右子树。
3 对于后序遍历，由于我们已经使用了最后一个元素作为根，剩下的部分被分为对应的左子树和右子树的后序遍历。
4 使用递归方法，先构造右子树，再构造左子树（因为后序遍历的顺序是左-右-根，所以我们在处理数组时应该从后向前）。
5 递归继续，直到数组为空，表示子树为空。
"""

class TreeNode:
    # 树节点的定义
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None  # 如果数组为空，返回空节点

        # 后序遍历的最后一个元素是根节点
        root = TreeNode(postorder[-1])
        root_index = inorder.index(postorder.pop())  # 找到根节点在中序遍历中的位置

        # 首先构造右子树，然后是左子树
        root.right = self.buildTree(inorder[root_index + 1:], postorder)
        root.left = self.buildTree(inorder[:root_index], postorder)

        return root

    def printTree(self, root):
        """将树以可读的格式打印"""
        if not root:
            return "null"
        return f"[{root.val}, {self.printTree(root.left)}, {self.printTree(root.right)}]"

# 使用例子测试代码
solution = Solution()

# 测试用例1
inorder1 = [9,3,15,20,7]
postorder1 = [9,15,7,20,3]
tree1 = solution.buildTree(inorder1, postorder1)

# 测试用例2
inorder2 = [-1]
postorder2 = [-1]
tree2 = solution.buildTree(inorder2, postorder2)

# 打印结果
output1 = solution.printTree(tree1)
output2 = solution.printTree(tree2)

output1, output2

