"""
要解决这个问题，我们可以使用图论中的概念。我们可以将每个变量视为图中的一个节点，每个等式Ai/Bi=value 可以表示为从
Ai 到 Bi 的有向边，边的权重是给定的值value。然后，对于每个查询 Cj/Dj，我们需要找到从 Cj 到
Dj 的路径，并计算沿途边的权重乘积。如果不存在这样的路径，或者查询中的变量在图中不存在，我们返回 -1.0。

1. 构建图：首先，我们需要构建一个图，其中每个变量都是图中的一个节点，每个等式则表示为两个节点之间的边。
    例如，对于等式 Ai/Bi=value，我们在节点 Ai 和 Bi 之间添加两条边，一条从 Ai 指向 Bi，权重为 value，
    另一条从 Bi 指向 Ai，权重为 1/value。

2. 查询处理：对于每个查询 Cj/Dj，我们需要在图中找到从 Cj 到 Dj 的路径，并沿着这条路径计算权重的乘积。
    如果不存在这样的路径，或者查询中涉及的变量在图中不存在，我们返回 -1.0。

3. 返回结果：根据上述处理，我们可以为每个查询计算出一个答案，并将所有答案组成一个列表返回。
"""

from collections import defaultdict

class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        def build_graph(equations: list[list[str]], values: list[float]) -> dict[str, dict[str, float]]:
            """
            构建图：将每个等式转换为图中的边。对于等式 Ai / Bi = value，添加两条边：
            一条从 Ai 到 Bi，权重为 value；
            另一条从 Bi 到 Ai，权重为 1 / value。
            """
            graph = defaultdict(dict)
            for (x, y), value in zip(equations, values):
                graph[x][y] = value
                graph[y][x] = 1.0 / value
            return graph

        def find_value(graph: dict[str, dict[str, float]], start: str, end: str, visited: set[str]) -> float:
            """
            查找值：通过深度优先搜索找到从 start 到 end 的路径，并计算路径上的权重乘积。
            如果在图中找不到这样的路径，或者其中一个变量在图中不存在，则返回 -1.0。
            """
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            visited.add(start)
            for neighbor in graph[start]:
                if neighbor not in visited:
                    # visited | {neighbor} 是set的并集运算符
                    temp_value = find_value(graph, neighbor, end, visited | {neighbor})
                    if temp_value != -1.0:
                        return graph[start][neighbor] * temp_value
            return -1.0

        # 构建图
        graph = build_graph(equations, values)

        # 处理查询并返回结果
        return [find_value(graph, query[0], query[1], set()) for query in queries]


def test_calcEquation():
    solution = Solution()

    # 测试用例1
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    expected = [6.0, 0.5, -1.0, 1.0, -1.0]
    assert solution.calcEquation(equations, values, queries) == expected, "测试用例1失败"

    # 测试用例2
    equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
    values = [1.5, 2.5, 5.0]
    queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
    expected = [3.75, 0.4, 5.0, 0.2]
    assert solution.calcEquation(equations, values, queries) == expected, "测试用例2失败"

    # 测试用例3
    equations = [["a", "b"]]
    values = [0.5]
    queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
    expected = [0.5, 2.0, -1.0, -1.0]
    assert solution.calcEquation(equations, values, queries) == expected, "测试用例3失败"

    print("所有测试用例通过")


if __name__ == "__main__":
    # 调用测试函数
    test_calcEquation()

