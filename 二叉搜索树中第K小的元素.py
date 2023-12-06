"""
给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。

输入：root = [3,1,4,null,2], k = 1
输出：1

输入：root = [5,3,6,2,4,null,null,1], k = 3
输出：3
 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 初始化结果和计数器
        self.k = k
        self.res = None
        self.count = 0

        # 中序遍历函数
        def inorder(node):
            if not node or self.count >= self.k:
                return
            # 首先遍历左子树
            inorder(node.left)
            # 访问当前节点
            self.count += 1
            if self.count == self.k:
                self.res = node.val
                return
            # 然后遍历右子树
            inorder(node.right)

        inorder(root)
        return self.res
