"""
这个问题是关于课程安排的，可以使用图论中的拓扑排序来解决。
拓扑排序是一种对有向图进行排序的算法，用于确定节点的线性顺序，使得对于每一条有向边 uv 从 u 到 v，u 都出现在 v 之前。

在这个问题中，每个课程可以看作是图中的一个节点，而先修关系可以看作是有向边。
如果能够进行拓扑排序，则意味着可以完成所有课程的学习。如果图中存在环，则无法完成所有课程（因为存在相互依赖的关系，形成了死锁）。

解题步骤如下：
1. 构建图：创建一个图，图中每个节点代表一个课程，有向边表示先修关系。
2. 计算入度：对于图中的每个节点，计算进入这个节点的边的数量，即该课程的先修课程数量。
3. 拓扑排序：创建一个队列，首先将所有入度为0的节点（即没有先修课程的课程）加入队列。
    然后开始循环，每次从队列中取出一个节点，并移除与它相连的边，这表示完成了这个课程的学习。
    每移除一条边，就将与之相连的节点的入度减1，如果某个节点的入度减为0，则将其加入队列。继续这个过程，直到队列为空。
4. 检查是否所有课程都被访问：如果所有课程都被加入过队列，则可以完成所有课程的学习，返回 true；否则，返回 false。
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 构建图（邻接表表示）和入度数组
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for cur, pre in prerequisites:
            graph[pre].append(cur)
            in_degree[cur] += 1

        # 将所有入度为0的课程加入队列
        queue = [i for i in range(numCourses) if in_degree[i] == 0]

        # 拓扑排序
        while queue:
            pre = queue.pop(0)
            for cur in graph[pre]:
                in_degree[cur] -= 1
                # 如果某个课程的入度为0，则加入队列
                if in_degree[cur] == 0:
                    queue.append(cur)

        # 检查是否所有课程的入度都为0
        return all(degree == 0 for degree in in_degree)
