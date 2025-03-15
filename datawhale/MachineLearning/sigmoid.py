import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')  # 或 'Agg'（如果是无界面环境）


# 定义 Sigmoid 函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 生成 x 轴数据
x = np.linspace(-10, 10, 400)
y = sigmoid(x)

# 绘制 Sigmoid 函数曲线
plt.figure(figsize=(6, 4))
plt.plot(x, y, label=r'$\sigma(x) = \frac{1}{1 + e^{-x}}$', color='blue')
plt.axhline(y=0, color='black', linewidth=0.5, linestyle='--')
plt.axhline(y=1, color='black', linewidth=0.5, linestyle='--')
plt.axvline(x=0, color='black', linewidth=0.5, linestyle='--')
plt.xlabel("x")
plt.ylabel(r"$\sigma(x)$")
plt.title("Sigmoid Function")
plt.legend()
plt.grid(True)

# 显示图像
plt.show()
