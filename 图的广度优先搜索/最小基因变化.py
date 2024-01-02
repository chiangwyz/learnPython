"""
这个问题可以通过建立一个基因序列的转换图，并利用广度优先搜索（BFS）来找到从起始序列到目标序列的最短路径来解决。
基因序列转换图是一个图，其中每个节点代表一个有效的基因序列，如果两个基因序列只有一个字符的差异，那么这两个节点之间就有一条边。

解题步骤如下：
1. 建立基因序列转换图：首先将 start 和 bank 中的所有序列作为节点加入图中。
  然后，对于图中的每个节点，找到与之只有一个基因差异的其他节点，并在这两个节点之间建立一条边。
2. 广度优先搜索：从 start 节点开始，进行广度优先搜索，直到找到 end 节点。
  在搜索过程中，记录每个节点到起点的距离（即变化次数）。
  当到达 end 节点时，所记录的距离就是最少变化次数。
3. 处理特殊情况：如果在 BFS 过程中无法到达 end 节点，或者 end 不在基因库 bank 中，那么返回 -1。
"""

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # 如果目标基因不在基因库中，直接返回-1
        if endGene not in bank:
            return -1

        # 将起始基因加入基因库
        bank = set(bank)
        bank.add(startGene)

        # 建立基因序列转换图
        graph = collections.defaultdict(list)
        for gene in bank:
            for i in range(len(gene)):
                for c in 'ACGT':
                    if c != gene[i]:
                        mutated = gene[:i] + c + gene[i+1:]
                        if mutated in bank:
                            graph[gene].append(mutated)

        # 广度优先搜索
        queue = collections.deque([(startGene, 0)])  # (基因序列, 变化次数)
        visited = set([startGene])
        while queue:
            gene, mutations = queue.popleft()
            if gene == endGene:
                return mutations
            for next_gene in graph[gene]:
                if next_gene not in visited:
                    visited.add(next_gene)
                    queue.append((next_gene, mutations + 1))

        return -1  # 如果找不到变化路径，返回-1

