"""
二叉树的最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。

为了计算二叉树的最大深度，我们可以使用递归的方法。
基本思想是比较左子树和右子树的深度，取其中较大的一个，并加上当前节点自身的深度。这里是相应的实现代码和注释：

这个方法遵循了分治法的思想，即将问题分解为子问题，分别解决后再将结果合并。
对于每一个节点，它的深度等于其左右子节点的最大深度加1。
递归的终止条件是当遇到空节点时返回 0，因为空节点不增加树的深度。
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 如果节点为空，深度为0
        if root is None:
            return 0

        # 递归计算左子树的深度
        left_depth = self.maxDepth(root.left)
        # 递归计算右子树的深度
        right_depth = self.maxDepth(root.right)

        # 当前节点的最大深度是左右子树深度的最大值加1（加的1是当前节点本身的深度）
        return max(left_depth, right_depth) + 1


import unittest


class TestMaxDepth(unittest.TestCase):
    def setUp(self):
        # 用于创建测试用的树的辅助函数
        def create_tree(level_order_values):
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

        self.solution = Solution()
        self.empty_tree = None
        self.single_node_tree = TreeNode(1)
        self.left_skewed_tree = create_tree([1, 2, 3, 4])
        self.right_skewed_tree = create_tree([4, 3, 2, 1])
        self.complete_tree = create_tree([1, 2, 3, 4, 5, 6, 7])
        self.normal_tree = create_tree([1, 2, 3, 4, 5])

    def test_empty_tree(self):
        self.assertEqual(self.solution.maxDepth(self.empty_tree), 0)

    def test_single_node_tree(self):
        self.assertEqual(self.solution.maxDepth(self.single_node_tree), 1)

    def test_left_skewed_tree(self):
        self.assertEqual(self.solution.maxDepth(self.left_skewed_tree), 3)

    def test_right_skewed_tree(self):
        self.assertEqual(self.solution.maxDepth(self.right_skewed_tree), 3)

    def test_complete_tree(self):
        self.assertEqual(self.solution.maxDepth(self.complete_tree), 3)

    def test_normal_tree(self):
        self.assertEqual(self.solution.maxDepth(self.normal_tree), 3)


if __name__ == '__main__':
    unittest.main()
