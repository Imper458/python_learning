import torch
import torch.nn as nn
import matplotlib.pyplot as plt


# 1.创建一个多元线性回归
class SimpleLinearRegression(nn.Module):
    def __init__(self):
        super(SimpleLinearRegression, self).__init__()
        # 创建一个全连接层，全连接层的输入维度是1，输出维度是1
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)


# 2.准备数据，自己构造一个数据
# y= 2x +1 +noise
x_data = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y_data = torch.tensor([[3.1], [5.2], [6.9], [8.9]])

# 3.创建模型、创建损失函数、创建优化器
model = SimpleLinearRegression()
criterion = nn.MSELoss()  # 回归任务最常用的损失函数
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

print("训练前的参数是：")
for param in model.parameters():
    print(f'{param.data}')

# 4.训练阶段
losses = []
for epoch in range(100):
    # 前向传播
    y_pred = model(x_data)  # y_pred = wx+b
    loss = criterion(y_pred, y_data)

    # 反向传播
    optimizer.zero_grad()  # 清除梯度
    loss.backward()
    optimizer.step()

    losses.append(loss.item())
    if epoch % 20 == 0:  # 每隔20次迭代打印一条信息
        print(f'epoch:[{epoch}/100],loss:{loss.item():.4f}')

print('\n训练后的参数：')
for name, param in model.named_parameters():
    print(f'name:{name},param:{param}')

# 可视化损失值的变化
plt.figure(figsize=(10, 4))  # 创建画布
# 在画布上面切分为左右两个子图
plt.subplot(1, 2, 1)
plt.plot(losses)
plt.title('Training Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
# 绘制原始的数据点
plt.subplot(1, 2, 2)
plt.scatter(x_data.numpy(), y_data.numpy(),label='True data')
#绘制拟合出来的模型，因为没有切换画布的位置
x_plot = (torch.linspace(0,6,100))#和np.linspace一样，都是在0到6创建100个点
x_plot = x_plot.reshape(-1,1)#把一维的数组reshape变成二维的数组
y_plot = model(x_plot).detach()
plt.plot(x_plot.numpy(),y_plot.numpy(),'r-',label='Fitted line')
plt.legend()#添加图例
plt.title('Linear Regression Result')
plt.tight_layout()
plt.show()
