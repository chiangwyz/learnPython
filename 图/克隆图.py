"""
要克隆一个无向连通图，我们可以使用深度优先搜索（DFS）或广度优先搜索（BFS）算法。
这里，我将展示如何使用深度优先搜索来实现。

在DFS过程中，我们需要确保每个节点只被访问一次以避免无限循环。
因此，我们需要一个哈希表来存储已经被访问并克隆的节点。哈希表的键是原始图中的节点，值是克隆图中的对应节点。

1. 检查给定的节点是否为空，如果是，则返回 None。
2. 如果节点已经在哈希表中，直接返回哈希表中的克隆节点。
3. 否则，创建一个新的节点作为原始节点的克隆，并将其添加到哈希表中。
4. 对于原始节点的每个邻居，递归调用克隆函数，并将返回的克隆邻居添加到克隆节点的邻居列表中。
5. 返回克隆的节点。

这个解决方案适用于无向连通图的深拷贝，并可以正确处理循环和共享节点。
"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # 使用哈希表存储已经访问并克隆的节点
        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]

            # 克隆节点
            clone_node = Node(node.val)
            visited[node] = clone_node

            # 克隆所有邻居节点
            for neighbor in node.neighbors:
                clone_node.neighbors.append(dfs(neighbor))

            return clone_node

        return dfs(node)
