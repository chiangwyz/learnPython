# generate_instances.py

import os
import json
import math
import random
import numpy as np

# -----------------------------
# 1. 定义各 Set（1~10）的固定参数
# -----------------------------
# 对应表 Table \ref{instance_table} 中的各列：
#   |V_FC|, |V_DC|, |V_CDP|, |V_C|, |P|, |\Pi_1|, |\Pi_2|
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
GRID_SIZE = 100  # 城市网格 100 x 100
FC_EDGE_OFFSET = 25  # FC 距离网格边界的距离
CT_CAPACITY = 1500
UV_CAPACITY = 500
CT_FIXED_COST = 1500
UV_FIXED_COST = 500
CDP_CAPACITY_LOW = int(0.2 * UV_CAPACITY)   # 100
CDP_CAPACITY_HIGH = int(0.6 * UV_CAPACITY)  # 300

# 客户服务时间窗参数
CUS_EARLIEST_START = 450
CUS_LATEST_END = 2550
CUS_SERVICE_DUR_MIN = 500
CUS_SERVICE_DUR_MAX = 2100  # 确保 CX 结束 <= 2550

# 库存-需求 比例集合
INVENTORY_RATIOS = [1.1, 1.2, 1.3, 1.4]

# 车辆单位行驶成本系数
COST_FACTOR = {
    'CDP': 1.0,
    'CT' : 1.2,
    'UV' : 1.1
}


# -----------------------------
# 2. 工具函数：随机生成位置、需求、库存、时间窗等
# -----------------------------
def sample_FC_positions(n_FC):
    """
    FC 坐标固定：距离边界 25 单位。如果 n_FC=2，则按(25,25),(75,75)；
               如果 n_FC=4，则按四个角 (25,25),(25,75),(75,25),(75,75)。
    """
    if n_FC == 2:
        return [(FC_EDGE_OFFSET, FC_EDGE_OFFSET),
                (GRID_SIZE - FC_EDGE_OFFSET, GRID_SIZE - FC_EDGE_OFFSET)]
    elif n_FC == 4:
        return [
            (FC_EDGE_OFFSET, FC_EDGE_OFFSET),
            (FC_EDGE_OFFSET, GRID_SIZE - FC_EDGE_OFFSET),
            (GRID_SIZE - FC_EDGE_OFFSET, FC_EDGE_OFFSET),
            (GRID_SIZE - FC_EDGE_OFFSET, GRID_SIZE - FC_EDGE_OFFSET)
        ]
    else:
        raise ValueError(f"目前只支持 n_FC=2 或 4，但传入 {n_FC}")


def sample_uniform_DC_positions(n_DC):
    """
    DC 坐标：在 [0,100]x[0,100] 区域内均匀随机分布。
    """
    xs = np.random.uniform(0, GRID_SIZE, size=n_DC)
    ys = np.random.uniform(0, GRID_SIZE, size=n_DC)
    return list(zip(xs.tolist(), ys.tolist()))


def sample_uniform_CDP_positions(n_CDP):
    """
    CDP 坐标：在 [0,100]x[0,100] 区域内均匀随机分布。
    """
    xs = np.random.uniform(0, GRID_SIZE, size=n_CDP)
    ys = np.random.uniform(0, GRID_SIZE, size=n_CDP)
    return list(zip(xs.tolist(), ys.tolist()))


def sample_uniform_customer_positions(n_C):
    """
    Customer 坐标：60% 在市中心 [25,75]x[25,75]，40% 在四个角的 25x25 区域（等概率分配到四个角）。
    返回一个长度为 n_C 的 (x,y) 列表。
    """
    n_center = int(round(0.6 * n_C))
    n_corner = n_C - n_center

    center_x = np.random.uniform(FC_EDGE_OFFSET, GRID_SIZE - FC_EDGE_OFFSET, size=n_center)
    center_y = np.random.uniform(FC_EDGE_OFFSET, GRID_SIZE - FC_EDGE_OFFSET, size=n_center)
    coords = [(center_x[i], center_y[i]) for i in range(n_center)]

    # 四个角落的子区域：分别是 [0,25]x[0,25]、[0,25]x[75,100]、[75,100]x[75,100]、[75,100]x[0,25]
    corner_regions = [
        (0, FC_EDGE_OFFSET, 0, FC_EDGE_OFFSET),
        (0, FC_EDGE_OFFSET, GRID_SIZE - FC_EDGE_OFFSET, GRID_SIZE),
        (GRID_SIZE - FC_EDGE_OFFSET, GRID_SIZE, GRID_SIZE - FC_EDGE_OFFSET, GRID_SIZE),
        (GRID_SIZE - FC_EDGE_OFFSET, GRID_SIZE, 0, FC_EDGE_OFFSET),
    ]
    for _ in range(n_corner):
        # 随机选一个角
        idx = random.randint(0, 3)
        x_low, x_high, y_low, y_high = corner_regions[idx]
        x = random.uniform(x_low, x_high)
        y = random.uniform(y_low, y_high)
        coords.append((x, y))

    # 打乱顺序，避免所有 center 在前，corner 在后
    random.shuffle(coords)
    return coords


def sample_customer_time_windows(n_C):
    """
    每个 Customer 有:
      - 固定最早服务时间 a_i=450
      - 服务时长 s_i ~ Uniform[500, 2100]
      - 最晚允许开始时间 b_i = 2550 - s_i
    返回一个列表 [(a_i, b_i, s_i)]，长度为 n_C
    """
    tw_list = []
    for _ in range(n_C):
        s_i = random.uniform(CUS_SERVICE_DUR_MIN, CUS_SERVICE_DUR_MAX)
        # 由于 s_i 有可能取到较大值，导致 b_i < a_i，需要剪裁 s_i，确保 b_i >= a_i
        if s_i > CUS_LATEST_END - CUS_EARLIEST_START:
            s_i = CUS_LATEST_END - CUS_EARLIEST_START
        a_i = CUS_EARLIEST_START
        b_i = CUS_LATEST_END - s_i
        tw_list.append((a_i, b_i, s_i))
    return tw_list


def sample_customer_demands(n_C, P):
    """
    每个 Customer i 包含 P 个物品：
      - 对于每个物品 p，需求 d_{i,p} ~ 从 {1,2,3,4} 中等概率抽取
    返回一个形状为 (n_C, P) 的需求矩阵（Python 嵌套列表）
    """
    demands = np.random.choice([1, 2, 3, 4], size=(n_C, P))
    return demands.tolist()


def sample_item_weights(P):
    """
    每个物品 p 的单位体积/重量 q_p ~ 从 {5,10,15} 中等概率抽取
    返回一个长度为 P 的列表 q = [q_1, q_2, ..., q_P]
    """
    return np.random.choice([5, 10, 15], size=P).tolist()


def allocate_inventory_to_FCs(n_FC, demands, inv_ratio):
    """
    1) 计算每个物品 p 的总体需求： sum_i d_{i,p}；
    2) 根据 inv_ratio，计算总库存： total_inv_p = ceil(inv_ratio * total_demand_p)；
    3) 将 total_inv_p 在 n_FC 个 FC 之间进行多项式分配，确保每个物品类别至少分配给两个 FC。
       这里先用 np.random.multinomial，然后如果某个物品只分配给了 1 个 FC，就随机从其他 FC 增加 1 单位库存并扣除原 FC 中 1 单位，直到至少有两个 FC > 0。
    返回一个形状为 (n_FC, P) 的库存矩阵（Python 嵌套列表）。
    """
    demands_arr = np.array(demands)  # (n_C, P)
    total_demand = demands_arr.sum(axis=0)  # 长度为 P

    # 生成每个物品 p 的总库存
    P = len(total_demand)
    total_inventory = np.ceil(inv_ratio * total_demand).astype(int)  # 长度为 P

    inv_matrix = np.zeros((n_FC, P), dtype=int)

    for p in range(P):
        # 如果 FC 数量小于 2，则无法保证“至少两个 FC”条件，但本问题 n_FC>=2
        # 首先进行多项式分配
        if total_inventory[p] >= n_FC:
            # 按均匀概率
            parts = np.random.multinomial(int(total_inventory[p]), [1.0 / n_FC] * n_FC)
        else:
            # 如果库存总数小于 FC 数量，先保证每个 FC 至少 0；多项式方式无法分出 1 个或 2 个 FC
            # 这时先随机从 total_inventory[p] 中挑 few 个 FC 放 1 单位库存
            parts = np.zeros(n_FC, dtype=int)
            chosen = np.random.choice(n_FC, int(total_inventory[p]), replace=False)
            parts[chosen] = 1

        # 检查至少有两个 FC > 0
        nonzero_fc = np.sum(parts > 0)
        if nonzero_fc < 2:
            # 随机挑一个已分配 >0 库存的 FC，减少 1，把库存给另一个 FC
            # 但如果本来只有一个 FC 得到库存，就把多余库存分给另一个 FC
            idx_nonzero = np.where(parts > 0)[0]
            idx_zero = np.where(parts == 0)[0]
            if len(idx_nonzero) == 0:
                # 所有 FC 都为 0，先随机选两个 FC 赋 1
                choose2 = np.random.choice(n_FC, 2, replace=False)
                parts[choose2[0]] = 1
                parts[choose2[1]] = total_inventory[p] - 1
            else:
                # 仅有一个 FC 非零
                idx_from = idx_nonzero[0]
                if total_inventory[p] > 1:
                    parts[idx_from] -= 1
                    # 从空闲 FC 中随机选一个进行补充
                    idx_to = np.random.choice(idx_zero, 1)[0]
                    parts[idx_to] += 1
                else:
                    # total_inventory[p] = 1，直接把 1 库存分给第二个 FC
                    parts[idx_from] = 0
                    idx_two = np.random.choice(n_FC, 2, replace=False)
                    parts[idx_two[0]] = 1
                    # 后面没有库存
            # 再次确保至少两个 FC>0
            # 如果还是不满足，就人为分配
            idx_nonzero = np.where(parts > 0)[0]
            if len(idx_nonzero) < 2:
                all_idx = list(range(n_FC))
                choose2 = np.random.choice(all_idx, 2, replace=False)
                parts[choose2[0]] = max(parts[choose2[0]], 1)
                parts[choose2[1]] = max(parts[choose2[1]], 1)

        inv_matrix[:, p] = parts

    return inv_matrix.tolist()  # 转成 Python 嵌套列表


# -----------------------------
# 3. 主函数：逐个 Set、每个 Set 生成 10 个实例
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
            # 为确保可复现，用 set_id 和 inst_id 共同决定随机种子
            seed =  1000 * set_id + inst_id
            random.seed(seed)
            np.random.seed(seed)

            # --------------- 3.1 生成各类节点的坐标 ---------------
            fc_positions   = sample_FC_positions(n_FC)
            dc_positions   = sample_uniform_DC_positions(n_DC)
            cdp_positions  = sample_uniform_CDP_positions(n_CDP)
            cust_positions = sample_uniform_customer_positions(n_C)

            # --------------- 3.2 生成 Customer 时间窗、需求 ---------------
            cust_time_windows = sample_customer_time_windows(n_C)  # [(a_i,b_i,s_i), ...]
            cust_demands = sample_customer_demands(n_C, P)        # [[d_{i,1},...,d_{i,P}], ...]

            # --------------- 3.3 生成物品重量 q_p ---------------
            item_weights = sample_item_weights(P)  # [q_1, q_2, ..., q_P]

            # --------------- 3.4 基于 demands 计算库存 ---------------
            inv_ratio = random.choice(INVENTORY_RATIOS)
            fc_inventory = allocate_inventory_to_FCs(n_FC, cust_demands, inv_ratio)
            # fc_inventory 是 (n_FC x P) 的矩阵

            # --------------- 3.5 生成 CDP 容量 Q_k ---------------
            cdp_capacities = []
            for _ in range(n_CDP):
                qk = random.randint(CDP_CAPACITY_LOW, CDP_CAPACITY_HIGH)
                cdp_capacities.append(qk)

            # --------------- 3.6 整理、打包实例信息 ----------------
            instance_data = {
                'set_id': set_id,
                'inst_id': inst_id,
                # 车辆信息
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
                # 物品相关
                'P': P,
                'item_weights': item_weights,   # q_p 列表
                # 库存-需求 比例
                'inventory_ratio': inv_ratio,
                # FC 节点列表
                'FCs': [
                    {
                        'id': f'FC{j+1}',
                        'x': float(fc_positions[j][0]),
                        'y': float(fc_positions[j][1]),
                        'time_window': [0, 3000],
                        'inventory': fc_inventory[j]  # 长度为 P 的列表
                    }
                    for j in range(n_FC)
                ],
                # DC 节点列表
                'DCs': [
                    {
                        'id': f'DC{j+1}',
                        'x': float(dc_positions[j][0]),
                        'y': float(dc_positions[j][1]),
                        'time_window': [300, 2700]
                    }
                    for j in range(n_DC)
                ],
                # CDP 节点列表
                'CDPs': [
                    {
                        'id': f'CDP{j+1}',
                        'x': float(cdp_positions[j][0]),
                        'y': float(cdp_positions[j][1]),
                        'time_window': [0, 3000],
                        'capacity': cdp_capacities[j]
                    }
                    for j in range(n_CDP)
                ],
                # Customer 节点列表
                'Customers': [
                    {
                        'id': f'C{j+1}',
                        'x': float(cust_positions[j][0]),
                        'y': float(cust_positions[j][1]),
                        'time_window': [cust_time_windows[j][0], cust_time_windows[j][1]],
                        'service_duration': cust_time_windows[j][2],
                        'demand': cust_demands[j]  # 长度为 P 的列表
                    }
                    for j in range(n_C)
                ]
            }

            # --------------- 3.7 写入 JSON 文件 ---------------
            filename = os.path.join(
                output_dir,
                f'instance_set{set_id}_{inst_id}.json'
            )
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(instance_data, f, ensure_ascii=False, indent=2)

            print(f"✓ 已生成：{filename}")

    print("==> 所有实例生成完毕，共 10x10 = 100 个 JSON 文件。")


if __name__ == '__main__':
    generate_all_instances()

