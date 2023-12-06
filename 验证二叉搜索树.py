"""
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：

节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

输入：root = [2,1,3]
输出：true

输入：root = [5,1,4,null,null,3,6]
输出：false
解释：根节点的值是 5 ，但是右子节点的值是 4 。

这段代码定义了一个辅助函数 validate，它会递归地检查每个节点是否符合二叉搜索树的条件。
我们在递归时更新每个节点的值应该在的范围。如果任何节点的值不在这个范围内，
或者它的子树不是有效的二叉搜索树，那么整个树就不是有效的二叉搜索树。
""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=float('-inf'), high=float('inf')):
            # 空节点默认是有效的
            if not node:
                return True
            
            # 当前节点的值必须在low和high之间
            if node.val <= low or node.val >= high:
                return False

            # 递归检查左子树和右子树
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        return validate(root)


