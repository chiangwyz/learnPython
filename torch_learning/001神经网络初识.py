import torch
from torch import nn

net = nn.Sequential(nn.Linear(2, 1))

# 假设我们有一个二维的输入
x = torch.tensor([[1.0, 2.0], [3.0, 4.0]])

# 进行前向传播
output = net(x)
print(output)
