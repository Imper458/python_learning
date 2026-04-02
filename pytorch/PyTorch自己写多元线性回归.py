import torch
import torch.nn as nn
from torch.autograd import backward


class SimpleLinearRegression(nn.Module):
    def __init__(self):
        super(SimpleLinearRegression, self).__init__()
        self.liner = nn.Linear(in_features=2, out_features=2)

    def forward(self, x):
        return self.liner(x)

#y=3x+2
x_data = torch.tensor([[1., 2.], [3., 4.], [5., 6.]])
y_data = torch.tensor([[4.8, 7.9], [11.0, 13.8], [20.6, 19.5]])
#创建模型
model = SimpleLinearRegression()
#创建损失函数
criterion = nn.MSELoss()
#创建优化器
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
print(optimizer)

losses = []
for epoch in range(100):
    #前向传播
    y_pred = model(x_data)
    loss = criterion(y_pred, y_data)
    #反向传播
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    losses.append(loss.item())
    if epoch % 10 == 0:
        print(f'Epoch {epoch}: Loss {loss.item():.4f}')

print('训练后的参数')
for name, param in model.named_parameters():
    print(name)
    print(param.data)




