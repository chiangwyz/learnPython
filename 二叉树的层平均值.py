"""
为了解决这个问题，我们可以使用广度优先搜索（BFS）来遍历二叉树的每一层。
在遍历每一层时，我们计算该层所有节点的总和并除以节点数量，得到该层的平均值。
下面是实现这个算法的步骤：

1.创建一个队列来存储每一层的节点。
2.将根节点加入队列。
3.遍历队列，直到队列为空：
  计算当前层的节点总数。
  遍历当前层的所有节点，计算节点值的总和。
  将每个节点的左右子节点加入队列（如果存在）。
  计算并存储当前层的平均值。
4.返回存储平均值的列表。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        averages = []  # 用于存储每层的平均值
        queue = collections.deque([root])  # 使用队列来存储每一层的节点

        while queue:
            level_length = len(queue)  # 当前层的节点数量
            level_sum = 0  # 当前层节点值的总和

            for _ in range(level_length):
                node = queue.popleft()  # 弹出当前节点
                level_sum += node.val  # 累加当前层的节点值

                # 如果左子节点存在，加入队列
                if node.left:
                    queue.append(node.left)
                # 如果右子节点存在，加入队列
                if node.right:
                    queue.append(node.right)

            # 计算当前层的平均值，并加入到averages列表中
            averages.append(level_sum / level_length)

        return averages
