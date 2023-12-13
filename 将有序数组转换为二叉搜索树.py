"""
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。
高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。

示例 1：
输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]
解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：

示例 2：
输入：nums = [1,3]
输出：[3,1]
解释：[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。

拓展知识：
在这里，提到的“高度差”指的是二叉树中每个节点的左右子树的高度差，而不是节点值的差异。
在二叉树中，一个节点的“高度”是指从该节点到最远叶子节点的最长路径的边数。

解题思路：
1. 找到中间元素：首先，我们需要找到数组的中间元素。
  由于数组已经是升序排列的，因此中间元素将成为二叉搜索树的根节点，这样可以确保树的平衡。
2. 构建左右子树：接着，我们将数组分成两部分——中间元素左边的部分用来构建左子树，右边的部分用来构建右子树。
  这样可以保证左子树中的所有元素都比根节点小，右子树中的所有元素都比根节点大。
3. 递归构建：我们递归地对左右两边的数组重复这个过程，直到数组为空。
  这样就可以构建出一个高度平衡的二叉搜索树。
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        # 如果数组为空，则返回空节点
        if not nums:
            return None

        # 找到数组的中间元素
        mid = len(nums) // 2

        # 创建一个新的树节点，其值为中间元素
        node = TreeNode(nums[mid])

        # 递归地构建左子树和右子树
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])

        return node

    def printTree(self, node, level=0):
        # 递归打印二叉树
        if node is not None:
            self.printTree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.val)
            self.printTree(node.left, level + 1)

# 示例
nums = [-10, -3, 0, 5, 9]
sol = Solution()
tree = sol.sortedArrayToBST(nums)
sol.printTree(tree)







