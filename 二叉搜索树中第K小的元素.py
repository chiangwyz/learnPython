"""
给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。

输入：root = [3,1,4,null,2], k = 1
输出：1

输入：root = [5,3,6,2,4,null,null,1], k = 3
输出：3

在这个 Python 代码示例中，k 和 res 被定义为类的成员变量（有时也称为实例变量），主要是为了在递归过程中方便地访问和修改这些变量的值。

如果 k 和 res 被定义为局部变量，那么在 inorder 内部递归函数中访问和修改它们会变得复杂。
因为 Python 的作用域规则限制了内部函数直接修改外部函数的局部变量。
虽然可以通过一些方法（如使用 nonlocal 关键字或者将它们封装为可变对象，比如列表）来解决这个问题，但这样会使代码变得更加复杂。

将这些变量定义为类的成员变量可以使得它们在类的所有方法中都可见和可修改，
这样就可以在 inorder 方法中方便地访问和更新这些值。
这种做法简化了代码，同时保持了清晰的逻辑结构，是处理类内部递归函数常见的实践。
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
