import torch
import torch.nn as nn
import matplotlib.pyplot as plt


# 1.创建一个多元线性回归
class MultipleLinearRegression(nn.Module):
    def __init__(self, input_dim):
        super(MultipleLinearRegression, self).__init__()
        # 创建一个全连接层，全连接层的输入维度是input_dim，输出维度是1
        self.linear = nn.Linear(input_dim, 1)

    def forward(self, x):
        return self.linear(x)


# 2.准备数据，自己构造一个数据
# y= 2x_1 +3x_2 +4x_3+1+noise
x_data = torch.tensor([[1.0, 2.0, 3.0],
                       [2.0, 3.0, 4.0],
                       [3.0, 4.0, 5.0],
                       [4.0, 5.0, 6.0]])
y_data = torch.tensor([[2 * 1.0 + 3 * 2.0 + 4 * 3.0 + 1 + 0.1],
                       [2 * 2.0 + 3 * 3.0 + 4 * 4.0 + 1 + 0.2],
                       [2 * 3.0 + 3 * 4.0 + 4 * 5.0 + 1 - 0.1],
                       [2 * 4.0 + 3 * 5.0 + 4 * 6.0 + 1 - 0.1]])

# 3.创建模型、创建损失函数、创建优化器
model = MultipleLinearRegression(input_dim=3)
criterion = nn.MSELoss()  # 回归任务最常用的损失函数
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

print("训练前的参数是：")
for name,param in model.named_parameters():
    print(f'{name}:{param.data}')

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

# 5.测试模型
test_x = torch.tensor([[5.0, 6.0, 7.0],])
prediction = model(test_x)
true_value = 2*5.0+3*6.0+4*7.0+1
print(f'\n预测 x = [5.0, 6.0, 7.0] y = {prediction.item():.4f}')
print(f'true_value:{true_value}')

#可视化损失
plt.figure(figsize=(10, 5))
plt.plot(losses)
plt.title('Training Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.show()