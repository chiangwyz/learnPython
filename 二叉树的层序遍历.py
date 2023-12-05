"""
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
1. 检查根节点是否为空：如果根节点为空，则返回空列表。
2. 初始化队列：创建一个队列并将根节点加入队列。
3. BFS 遍历：
    当队列不为空时，循环处理队列中的节点。
    对于每一层，初始化一个空列表来存储该层的节点值。
    记录当前层的节点数（即当前队列的长度）。
    对于当前层的每个节点，将其值添加到列表中，并将其左右子节点（如果存在的话）加入队列。
    将该层的节点值列表添加到最终结果中。
4. 返回结果：返回包含每层节点值的列表。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
        
        result = []
        queue = collections.deque([root])

        while queue:
            level_length = len(queue)

            tmp = []
            for _ in range(level_length):
                node = queue.popleft()
                tmp.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(tmp)

        return result
