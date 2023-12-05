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

在代码中，collections.deque([root]) 用于创建一个队列，以便进行树的层次遍历（BFS - 广度优先搜索）。
在遍历过程中，您会从队列的前端删除节点（使用 popleft），并从后端插入新的节点（使用 append）。
这种操作方式使得队列始终按照从上到下、从左到右的顺序保存树的节点，从而实现层次遍历。

在使用 collections.deque 进行二叉树的层次遍历时，确实是通过这样的方式来控制访问的。具体来说：

1.通过 popleft() 弹出当前层的节点：在每一层的遍历开始时，队列中包含的都是当前层的节点。
使用 popleft() 方法从队列的前端移除并返回这些节点，这样可以保证按照从左到右的顺序处理当前层的每个节点。

2.通过 append 添加下一层的节点：在处理当前层的每个节点时，检查该节点的左右子节点。
如果存在子节点，则通过 append 方法将这些子节点添加到队列的末尾。这样做会将下一层的节点加入队列中，但它们会排在当前层剩余节点的后面。

3.通过 level_length 控制不会访问到下一层的节点：在开始遍历当前层之前，通过 len(queue) 获取当前层节点的数量（即 level_length）。
然后使用一个 for 循环来遍历这些节点。由于 level_length 是在添加下一层节点之前确定的，
所以这个循环只会处理当前层的节点，而不会触及下一层的任何节点。

通过这种方式，代码能够确保在计算每层的平均值时，只会考虑当前层的节点，
并且在处理完所有当前层的节点之后，队列中仅包含下一层的节点。这个过程会一直重复，直到遍历完整棵树的所有层。
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
