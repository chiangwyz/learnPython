import networkx as nx
import matplotlib.pyplot as plt

# 创建一个二部图
bipartite_graph = nx.Graph()

# 示例任务和机器
unassigned_tasks = [0, 1, 2]
num_machines = 2
task_node_group_ind = 0
machine_group_node_ind = 1

# 添加任务节点
bipartite_graph.add_nodes_from(
    [f't-{task_id}' for task_id in unassigned_tasks],
    bipartite=task_node_group_ind
)

# 添加机器节点
bipartite_graph.add_nodes_from(
    [f'm-{machine_id}' for machine_id in range(num_machines)],
    bipartite=machine_group_node_ind
)

# 添加边（这里假设所有任务到所有机器的边权重都是 1）
bipartite_graph.add_weighted_edges_from(
    (f't-{task_id}', f'm-{machine_id}', task_id+machine_id)
    for task_id in unassigned_tasks
    for machine_id in range(num_machines)
)

assert nx.is_bipartite(bipartite_graph)
minimum_weight_matching = nx.algorithms.min_weight_matching(bipartite_graph)


def _unwrap(assignment) -> tuple[int, int]:
    first, second = assignment
    if first[0] == 't':
        print("t\n")
        print("first", first)
        print("second", second)
        return int(first[2:]), int(second[2:])
    else:
        print("m\n")
        print("first", first)
        print("second", second)
        return int(second[2:]), int(first[2:])


for assignment in minimum_weight_matching:
    task_id, machine_id = _unwrap(assignment)
    print("({}, {})".format(task_id, machine_id))

# 获取节点的二部图布局
pos = {}
pos.update((node, (1, index)) for index, node in enumerate([f't-{task_id}' for task_id in unassigned_tasks]))  # 将任务节点放在左侧
pos.update((node, (2, index)) for index, node in enumerate([f'm-{machine_id}' for machine_id in range(num_machines)]))  # 将机器节点放在右侧

# 绘制二部图
plt.figure(figsize=(12, 8))
nx.draw(bipartite_graph, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold')
labels = nx.get_edge_attributes(bipartite_graph, 'weight')
nx.draw_networkx_edge_labels(bipartite_graph, pos, edge_labels=labels, label_pos=0.3)  # 调整 label_pos 参数


# 显示图像
plt.show()
