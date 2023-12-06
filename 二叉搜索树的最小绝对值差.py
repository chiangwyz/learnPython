"""

为了找到二叉搜索树中任意两个不同节点值之间的最小差值，我们可以利用二叉搜索树的一个重要性质：它的中序遍历序列是递增的。
因此，最小差值一定出现在中序遍历序列中相邻的两个节点之间。

这里是一个解决方案的步骤：

1. 中序遍历树：对树进行中序遍历，并将节点值存储在一个列表中。

2. 计算最小差值：遍历这个列表，计算相邻元素之间的差值，找出最小的差值。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # 用于存储中序遍历结果的列表
        values = []

        # 中序遍历树，并将值存储到列表中
        def inorder(node):
            if node:
                inorder(node.left)
                values.append(node.val)
                inorder(node.right)
        
        # 执行中序遍历
        inorder(root)

        # 计算并返回相邻元素之间的最小差值
        return min(values[i + 1] - values[i] for i in range(len(values) - 1))

# 示例用法
# root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
# solution = Solution()
# result = solution.getMinimumDifference(root)
# print(result)  # 输出应该是 1




