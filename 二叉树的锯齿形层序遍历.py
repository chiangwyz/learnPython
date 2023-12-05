"""
要实现这个锯齿形层序遍历二叉树的功能，我们可以使用广度优先搜索（BFS）。
在这种遍历方式中，我们使用一个队列来存储每一层的节点，并交替改变遍历的方向。

以下是具体的实现步骤和代码，包含中文注释以便理解：

1 检查空树：如果树为空，直接返回空列表。
2 初始化：使用一个队列来存储节点，并将根节点入队。
    同时，我们需要一个变量来表示当前层的遍历方向。
3 层序遍历：当队列不为空时，我们遍历当前层的所有节点。
    在每一层的开始，我们创建一个临时列表来存储这一层的节点值。
4 节点处理：对于当前层的每个节点，我们将其值添加到临时列表中。
    然后，我们检查并将其子节点（如果有的话）按照左子节点和右子节点的顺序加入队列中。
5 方向调整：在完成当前层的遍历后，根据当前的遍历方向，我们决定是直接将这一层的结果添加到最终结果中，还是先将其反转后再添加。
6 切换方向：切换遍历方向以便于下一层的遍历。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = collections.deque([root])
        left_to_right = True  # 初始方向为从左到右

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.popleft()

                # 根据当前方向添加节点值
                if left_to_right:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)

                # 将子节点加入队列
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)
            left_to_right = not left_to_right  # 切换方向

        return result







