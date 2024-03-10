"""
为了检查一个二叉树是否轴对称，我们可以使用递归的方法。
基本思路是比较树的左子树和右子树是否是镜像对称的。
对于两个子树来说，要满足以下条件才能认为它们是对称的：

两个子树的根节点的值相同。
左子树的左子节点和右子树的右子节点对称（它们的值相同，且子树结构对称）。
左子树的右子节点和右子树的左子节点对称。
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 空树被视为对称的
        if not root:
            return True  

        # 检查左右子树是否为镜像
        return self.isMirror(root.left, root.right)  

    def isMirror(self, left: TreeNode, right: TreeNode) -> bool:
        # 两个空节点视为对称
        if not left and not right:
            return True  
        # 一个节点为空，另一个不为空，不对称
        if not left or not right:
            return False  
        # 两个节点的值不同，不对称
        if left.val != right.val:
            return False  

        # 递归检查当前节点的左右子节点是否为镜像
        return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)


import unittest


class TestSymmetricTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # 用于创建测试用的树的辅助函数
    def create_tree(self, level_order_values: list):
        """
        按层序遍历数组生成二叉树。
        :param level_order_values: 一个整数列表，其中None表示没有节点。
        :return: 树的根节点。
        """
        if not level_order_values or level_order_values[0] is None:
            return None

        root = TreeNode(level_order_values[0])
        queue = [root]
        index = 1

        while index < len(level_order_values):
            current = queue.pop(0)

            # 添加左子节点
            if index < len(level_order_values) and level_order_values[index] is not None:
                current.left = TreeNode(level_order_values[index])
                queue.append(current.left)
            index += 1

            # 添加右子节点
            if index < len(level_order_values) and level_order_values[index] is not None:
                current.right = TreeNode(level_order_values[index])
                queue.append(current.right)
            index += 1

        return root

    def test_symmetric_tree(self):
        # 测试用例1: 对称的树
        tree = self.create_tree([1, 2, 2, 3, 4, 4, 3])
        self.assertTrue(self.solution.isSymmetric(tree), "The tree is symmetric but was not recognized as such.")

        # 测试用例2: 不对称的树
        tree = self.create_tree([1, 2, 2, None, 3, None, 3])
        self.assertFalse(self.solution.isSymmetric(tree),
                         "The tree is not symmetric but was recognized as symmetric.")

        # 测试用例3: 空树
        tree = self.create_tree([])
        self.assertTrue(self.solution.isSymmetric(tree), "The empty tree should be considered symmetric.")

        # 测试用例4: 只有根节点的树
        tree = self.create_tree([1])
        self.assertTrue(self.solution.isSymmetric(tree), "The single-node tree should be considered symmetric.")

        # 测试用例5: 完全对称的复杂树
        tree = self.create_tree([1, 2, 2, 3, 4, 4, 3, 5, None, None, 5, 5, None, None, 5])
        self.assertTrue(self.solution.isSymmetric(tree),
                        "The complex symmetric tree was not recognized as symmetric.")

        # 测试用例6: 含有None值的对称树
        tree = self.create_tree([1, 2, 2, None, 3, 3, None])
        self.assertTrue(self.solution.isSymmetric(tree),
                        "The tree with None values is symmetric but was not recognized as such.")


if __name__ == "__main__":
    unittest.main()