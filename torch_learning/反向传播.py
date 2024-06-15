import torch_learning

# 创建一个张量，并启用自动求导
x = torch_learning.tensor([1.0, 2.0, 3.0], requires_grad=True)

# 清除之前的梯度值
x.grad = torch_learning.zeros_like(x)  # 或者 x.grad.zero_()，但第一次需要初始化

# 计算损失
y = x.sum()

# 执行反向传播
y.backward()

# 查看梯度
print(x.grad)
