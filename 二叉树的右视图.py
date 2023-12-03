"""
给定一个二叉树的 根节点 root，想象自己站在它的右侧，
按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例 1:
输入: [1,2,3,null,5,null,4]
输出: [1,3,4]

示例 2:
输入: [1,null,3]
输出: [1,3]

示例 3:
输入: []
输出: []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

核心思路：
使用层序遍历（广度优先搜索）来遍历二叉树的每一层。
在每一层中，记录最后一个节点的值，因为这是从右侧看到的节点。
"""

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []  # 如果树为空，则返回空列表

        queue = collections.deque([root])  # 使用双端队列初始化，开始时只有根节点
        rightside = []  # 存储每一层最右侧节点的值

        while queue:
            level_length = len(queue)  # 获取当前层的节点数量
            for i in range(level_length):  # 遍历当前层的每个节点
                node = queue.popleft()  # 弹出一个节点
                if i == level_length - 1:  # 如果是当前层的最后一个节点
                    rightside.append(node.val)  # 将其值添加到结果列表
                if node.left:  # 如果节点有左子节点
                    queue.append(node.left)  # 将左子节点添加到队列
                if node.right:  # 如果节点有右子节点
                    queue.append(node.right)  # 将右子节点添加到队列

        return rightside  # 返回最终结果









