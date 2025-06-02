# generate_instances.py

import os
import json
import matplotlib.pyplot as plt
import math
import random
import numpy as np


# -----------------------------
# 1. 定义各 Set（1~10）的固定参数
# -----------------------------
SET_PARAMS = {
    1:  {'n_FC': 2, 'n_DC': 4,  'n_CDP': 10,  'n_C': 20,  'P': 2, 'Pi1': 4,  'Pi2': 8},
    2:  {'n_FC': 2, 'n_DC': 4,  'n_CDP': 12,  'n_C': 20,  'P': 3, 'Pi1': 6,  'Pi2': 8},
    3:  {'n_FC': 2, 'n_DC': 4,  'n_CDP': 16,  'n_C': 20,  'P': 4, 'Pi1': 8,  'Pi2': 12},
    4:  {'n_FC': 2, 'n_DC': 4,  'n_CDP': 16,  'n_C': 36,  'P': 3, 'Pi1': 8,  'Pi2': 16},
    5:  {'n_FC': 2, 'n_DC': 4,  'n_CDP': 20,  'n_C': 50,  'P': 3, 'Pi1': 10, 'Pi2': 20},
    6:  {'n_FC': 2, 'n_DC': 4,  'n_CDP': 30,  'n_C': 50,  'P': 3, 'Pi1': 10, 'Pi2': 20},
    7:  {'n_FC': 4, 'n_DC': 8,  'n_CDP': 40,  'n_C': 80,  'P': 3, 'Pi1': 16, 'Pi2': 32},
    8:  {'n_FC': 4, 'n_DC': 8,  'n_CDP': 50,  'n_C': 100, 'P': 3, 'Pi1': 20, 'Pi2': 40},
    9:  {'n_FC': 4, 'n_DC': 8,  'n_CDP': 100, 'n_C': 200, 'P': 3, 'Pi1': 32, 'Pi2': 64},
    10: {'n_FC': 4, 'n_DC': 8,  'n_CDP': 200, 'n_C': 400, 'P': 3, 'Pi1': 56, 'Pi2': 96},
}

# 固定常量
GRID_SIZE = 100                # 城市网格大小 100 x 100
FC_EDGE_OFFSET = 25            # FC 距离网格边界的偏移
CT_CAPACITY = 1500
UV_CAPACITY = 500
CT_FIXED_COST = 1500
UV_FIXED_COST = 500
CDP_CAPACITY_LOW = int(0.2 * UV_CAPACITY)   # 100
CDP_CAPACITY_HIGH = int(0.6 * UV_CAPACITY)  # 300

# Customer 时间窗参数
CUS_EARLIEST_START = 450
CUS_LATEST_END = 2550
CUS_SERVICE_MIN = 500
CUS_SERVICE_MAX = 2150

# 库存-需求 比例集合
INVENTORY_RATIOS = [1.1, 1.2, 1.3, 1.4]

# 单位行驶成本系数
COST_FACTOR = {'CDP': 1.0, 'CT': 1.2, 'UV': 1.1}


# -----------------------------
# 2. 工具函数
# -----------------------------
def sample_FC_positions(n_FC):
    """
    FC 坐标固定：距离边界 25 单位。
    如果 n_FC=2，则用 (25,25), (75,75)。
    如果 n_FC=4，则用四个角 (25,25), (25,75), (75,25), (75,75)。
    返回时都四舍五入到两位小数。
    """
    if n_FC == 2:
        return [(round(FC_EDGE_OFFSET, 2), round(FC_EDGE_OFFSET, 2)),
                (round(GRID_SIZE - FC_EDGE_OFFSET, 2), round(GRID_SIZE - FC_EDGE_OFFSET, 2))]
    elif n_FC == 4:
        return [(round(FC_EDGE_OFFSET, 2), round(FC_EDGE_OFFSET, 2)),
                (round(FC_EDGE_OFFSET, 2), round(GRID_SIZE - FC_EDGE_OFFSET, 2)),
                (round(GRID_SIZE - FC_EDGE_OFFSET, 2), round(FC_EDGE_OFFSET, 2)),
                (round(GRID_SIZE - FC_EDGE_OFFSET, 2), round(GRID_SIZE - FC_EDGE_OFFSET, 2))]
    else:
        raise ValueError(f"目前只支持 n_FC=2 或 4，但传入 {n_FC}")

def sample_uniform_positions(n, low, high):
    """
    在 [low, high] x [low, high] 区域里随机均匀采样 n 个点，
    返回坐标列表并四舍五入到两位小数。
    """
    xs = np.random.uniform(low, high, size=n)
    ys = np.random.uniform(low, high, size=n)
    return [(round(xs[i], 2), round(ys[i], 2)) for i in range(n)]

def sample_uniform_customer_positions(n_C):
    """
    Customer 坐标方案：
      - 60% 的点在市中心 [25,75] x [25,75]
      - 40% 的点均匀分布在四个角的 25x25 子区域：
          [0,25]x[0,25], [0,25]x[75,100], [75,100]x[75,100], [75,100]x[0,25]
    返回长度为 n_C 的列表，每个 (x,y) 四舍五入到两位小数。
    """
    n_center = int(round(0.6 * n_C))
    n_corner = n_C - n_center

    # 市中心部分
    center_x = np.random.uniform(FC_EDGE_OFFSET, GRID_SIZE - FC_EDGE_OFFSET, size=n_center)
    center_y = np.random.uniform(FC_EDGE_OFFSET, GRID_SIZE - FC_EDGE_OFFSET, size=n_center)
    coords = [(round(center_x[i], 2), round(center_y[i], 2)) for i in range(n_center)]

    # 四个角的子区域
    corner_regions = [
        (0, FC_EDGE_OFFSET, 0, FC_EDGE_OFFSET),
        (0, FC_EDGE_OFFSET, GRID_SIZE - FC_EDGE_OFFSET, GRID_SIZE),
        (GRID_SIZE - FC_EDGE_OFFSET, GRID_SIZE, GRID_SIZE - FC_EDGE_OFFSET, GRID_SIZE),
        (GRID_SIZE - FC_EDGE_OFFSET, GRID_SIZE, 0, FC_EDGE_OFFSET),
    ]
    for _ in range(n_corner):
        idx = random.randint(0, 3)
        x_low, x_high, y_low, y_high = corner_regions[idx]
        x = random.uniform(x_low, x_high)
        y = random.uniform(y_low, y_high)
        coords.append((round(x, 2), round(y, 2)))

    random.shuffle(coords)
    return coords

def sample_customer_time_windows(n_C):
    """
    为每个客户生成时间窗 [450.00, end_time]：
      - 先 s_i ~ Uniform[500,2150]
      - end = 450 + s_i
      - 如果 end > 2550，则强制 end = 2550
    返回一个长度为 n_C 的列表，形如 [[450.00, end_i], ...]
    """
    tw_list = []
    for _ in range(n_C):
        s_i = random.uniform(CUS_SERVICE_MIN, CUS_SERVICE_MAX)
        end = CUS_EARLIEST_START + s_i
        if end > CUS_LATEST_END:
            end = CUS_LATEST_END
        tw_list.append([round(450.00, 2), round(end, 2)])
    return tw_list

def sample_customer_demands(n_C, P):
    """
    每个客户 i 有 P 件物品，需求 d_{i,p} ~ Uniform 从 {1,2,3,4}。
    返回形状 (n_C, P) 的整型列表。
    """
    demands = np.random.choice([1, 2, 3, 4], size=(n_C, P))
    return demands.tolist()

def sample_item_weights(P):
    """
    每个物品 p 的体积/重量 q_p ~ 从 {5,10,15} 中等概率抽取。
    返回长度为 P 的列表，整数即可。
    """
    return np.random.choice([5, 10, 15], size=P).tolist()

def allocate_inventory_to_FCs(n_FC, demands, inv_ratio):
    """
    方法：
      1. 计算每个物品 p 的总需求 sum_i d_{i,p}
      2. 总库存 total_inventory_p = ceil(inv_ratio * 总需求_p)
      3. 用 np.random.multinomial 在 n_FC 个 FC 之间分配 total_inventory_p，
         确保至少有两个 FC>0（若不满足则做微调）。
    返回：
      inv_matrix (n_FC x P) 的整型列表，每行表示该 FC 每个物品的库存。

    且断言 sum(inv_matrix[:, p]) == total_inventory_p
    """
    demands_arr = np.array(demands)
    total_demand = demands_arr.sum(axis=0)  # 长度 P
    P = len(total_demand)
    total_inventory = np.ceil(inv_ratio * total_demand).astype(int)
    inv_matrix = np.zeros((n_FC, P), dtype=int)

    for p in range(P):
        Ti = int(total_inventory[p])
        if Ti >= n_FC:
            parts = np.random.multinomial(Ti, [1.0 / n_FC] * n_FC)
        else:
            parts = np.zeros(n_FC, dtype=int)
            chosen = np.random.choice(n_FC, Ti, replace=False)
            parts[chosen] = 1

        # 确保至少有两个 FC>0
        nonzero_fc = np.sum(parts > 0)
        if nonzero_fc < 2:
            idx_nonzero = np.where(parts > 0)[0]
            idx_zero = np.where(parts == 0)[0]
            if len(idx_nonzero) == 0:
                choose2 = np.random.choice(n_FC, 2, replace=False)
                parts[choose2[0]] = 1
                parts[choose2[1]] = Ti - 1 if Ti > 1 else 1
            else:
                idx_from = idx_nonzero[0]
                if Ti > 1:
                    parts[idx_from] -= 1
                    idx_to = np.random.choice(idx_zero, 1)[0]
                    parts[idx_to] += 1
                else:
                    parts[idx_from] = 0
                    idx_two = np.random.choice(n_FC, 2, replace=False)
                    parts[idx_two[0]] = 1
                    parts[idx_two[1]] = 0
            idx_nonzero = np.where(parts > 0)[0]
            if len(idx_nonzero) < 2:
                all_idx = list(range(n_FC))
                choose2 = np.random.choice(all_idx, 2, replace=False)
                parts[choose2[0]] = max(parts[choose2[0]], 1)
                parts[choose2[1]] = max(parts[choose2[1]], 1)

        # 确保分配总量等于 total_inventory[p]
        assert parts.sum() == Ti, f"Inventory sum mismatch for item {p}: {parts.sum()} != {Ti}"
        inv_matrix[:, p] = parts

    return inv_matrix.tolist()


# -----------------------------
# 3. 主函数：生成所有实例
# -----------------------------
def generate_all_instances(output_dir='instances'):
    os.makedirs(output_dir, exist_ok=True)

    for set_id in range(1, 11):
        params = SET_PARAMS[set_id]
        n_FC = params['n_FC']
        n_DC = params['n_DC']
        n_CDP = params['n_CDP']
        n_C = params['n_C']
        P = params['P']
        n_CT = params['Pi1']
        n_UV = params['Pi2']

        for inst_id in range(1, 11):
            # 固定种子保证可复现
            seed = 1000 * set_id + inst_id
            random.seed(seed)
            np.random.seed(seed)

            # 3.1 生成各节点坐标
            fc_positions = sample_FC_positions(n_FC)
            dc_positions = sample_uniform_positions(n_DC, 0, GRID_SIZE)
            cdp_positions = sample_uniform_positions(n_CDP, 0, GRID_SIZE)
            cust_positions = sample_uniform_customer_positions(n_C)

            # 3.2 生成客户时间窗 & 需求
            cust_time_windows = sample_customer_time_windows(n_C)
            cust_demands = sample_customer_demands(n_C, P)

            # 3.3 生成物品重量、库存
            item_weights = sample_item_weights(P)
            inv_ratio = random.choice(INVENTORY_RATIOS)
            fc_inventory = allocate_inventory_to_FCs(n_FC, cust_demands, inv_ratio)

            # 3.4 生成 CDP 容量
            cdp_capacities = [random.randint(CDP_CAPACITY_LOW, CDP_CAPACITY_HIGH) for _ in range(n_CDP)]

            # 3.5 打包实例
            instance_data = {
                'set_id': set_id,
                'inst_id': inst_id,
                'vehicles': {
                    'CT': {
                        'count': n_CT,
                        'capacity': CT_CAPACITY,
                        'fixed_cost': CT_FIXED_COST,
                        'unit_cost_factor': COST_FACTOR['CT']
                    },
                    'UV': {
                        'count': n_UV,
                        'capacity': UV_CAPACITY,
                        'fixed_cost': UV_FIXED_COST,
                        'unit_cost_factor': COST_FACTOR['UV']
                    }
                },
                'P': P,
                'item_weights': item_weights,
                'inventory_ratio': round(inv_ratio, 2),
                'FCs': [
                    {
                        'id': f'FC{j+1}',
                        'x': fc_positions[j][0],
                        'y': fc_positions[j][1],
                        'time_window': [0.00, 3000.00],
                        'inventory': fc_inventory[j]
                    }
                    for j in range(n_FC)
                ],
                'DCs': [
                    {
                        'id': f'DC{j+1}',
                        'x': dc_positions[j][0],
                        'y': dc_positions[j][1],
                        'time_window': [300.00, 2700.00]
                    }
                    for j in range(n_DC)
                ],
                'CDPs': [
                    {
                        'id': f'CDP{j+1}',
                        'x': cdp_positions[j][0],
                        'y': cdp_positions[j][1],
                        'time_window': [0.00, 3000.00],
                        'capacity': cdp_capacities[j]
                    }
                    for j in range(n_CDP)
                ],
                'Customers': [
                    {
                        'id': f'C{j+1}',
                        'x': cust_positions[j][0],
                        'y': cust_positions[j][1],
                        'time_window': cust_time_windows[j],
                        'demand': cust_demands[j]
                    }
                    for j in range(n_C)
                ]
            }

            # 3.6 写入 JSON
            filename = os.path.join(output_dir, f'instance_set{set_id}_{inst_id}.json')
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(instance_data, f, ensure_ascii=False, indent=2)

            print(f"✓ 已生成：{filename}")

    print("==> 所有实例生成完毕，共 10x10 = 100 个 JSON 文件。")


def plot_instance_nodes(instance_path):
    """
    读取给定路径的实例 JSON 文件，并绘制其中的 FC、DC、CDP、Customer 节点位置。
    """
    with open(instance_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 提取各类节点坐标
    fc_coords = [(fc['x'], fc['y']) for fc in data['FCs']]
    dc_coords = [(dc['x'], dc['y']) for dc in data['DCs']]
    cdp_coords = [(cdp['x'], cdp['y']) for cdp in data['CDPs']]
    cust_coords = [(c['x'], c['y']) for c in data['Customers']]

    # 分别拆分成 x, y 列表
    fc_x, fc_y = zip(*fc_coords) if fc_coords else ([], [])
    dc_x, dc_y = zip(*dc_coords) if dc_coords else ([], [])
    cdp_x, cdp_y = zip(*cdp_coords) if cdp_coords else ([], [])
    cust_x, cust_y = zip(*cust_coords) if cust_coords else ([], [])

    plt.figure(figsize=(8, 8))
    # 绘制
    plt.scatter(fc_x, fc_y, marker='s', label='FC (Fulfillment Center)')
    plt.scatter(dc_x, dc_y, marker='D', label='DC (Distribution Center)')
    plt.scatter(cdp_x, cdp_y, marker='^', label='CDP')
    plt.scatter(cust_x, cust_y, marker='o', label='Customer')

    plt.title(f"节点分布：实例 {data['set_id']}-{data['inst_id']}")
    plt.xlabel("X 坐标")
    plt.ylabel("Y 坐标")
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    # generate_all_instances()

    # 示例：绘制实例文件 "instances/instance_set1_1.json" 的节点位置
    plot_instance_nodes("instances/instance_set7_10.json")
