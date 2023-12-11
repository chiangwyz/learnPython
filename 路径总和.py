"""
可以使用递归方法遍历二叉树，从根节点开始，沿着每条路径向下走，直到到达叶子节点。
在遍历过程中，我们需要跟踪到目前为止路径上所有节点的总和，并与目标和targetSum进行比较。

解题思路如下：

递归终止条件：当遍历到叶子节点时，检查当前路径的总和是否等于targetSum。
递归过程：对于每个非叶子节点，我们递归地检查其左右子树。
路径和更新：在遍历的过程中，我们需要更新路径上节点的总和。
返回值：如果在任何叶子节点处找到路径和等于targetSum，则返回True，否则返回False。

在这段代码中，check_path_sum是一个递归函数，它负责遍历树并计算路径和。
当遍历到叶子节点时，会检查当前路径的总和是否与targetSum相等。
如果在树中找到了这样的路径，则返回True；否则，遍历完整棵树后返回False。

拓展知识：
叶子节点的定义：在二叉树中，叶子节点是指没有子节点的节点。也就是说，一个叶子节点既没有左子节点也没有右子节点。
"""

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # 如果根节点为空，则直接返回False
        if not root:
            return False

        # 递归函数，用于遍历树并检查路径和
        def check_path_sum(node, current_sum):
            # 如果当前节点为空，返回False
            if not node:
                return False

            # 更新当前路径和
            current_sum += node.val

            # 检查当前节点是否是叶子节点
            if not node.left and not node.right:
                # 如果是叶子节点，检查当前路径和是否等于目标和
                return current_sum == targetSum

            # 递归检查左右子树
            return check_path_sum(node.left, current_sum) or check_path_sum(node.right, current_sum)

        # 从根节点开始，初始路径和为0
        return check_path_sum(root, 0)
