#手写识别项目

# import torch
# import torch.nn as nn
# import torch.nn.functional as F
# import torch.optim as optim
# from torchvision import datasets, transforms
# import matplotlib.pyplot as plt
#
# # 1️⃣ 数据准备
# transform = transforms.Compose([
#     transforms.ToTensor(),
#     transforms.Normalize((0.5,), (0.5,))
# ])
# train_data = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
# test_data = datasets.MNIST(root='./data', train=False, download=True, transform=transform)
#
# train_loader = torch.utils.data.DataLoader(train_data, batch_size=64, shuffle=True)
# test_loader = torch.utils.data.DataLoader(test_data, batch_size=1000, shuffle=False)
#
# # 2️⃣ 定义 CNN 模型
# class CNN(nn.Module):
#     def __init__(self):
#         super(CNN, self).__init__()
#         self.conv1 = nn.Conv2d(1, 32, 3, 1)
#         self.conv2 = nn.Conv2d(32, 64, 3, 1)
#         self.pool = nn.MaxPool2d(2)
#         self.fc1 = None  # 先不定义，稍后根据输入动态创建
#         self.fc2 = nn.Linear(128, 10)
#
#     def forward(self, x):
#         x = F.relu(self.conv1(x))
#         x = self.pool(F.relu(self.conv2(x)))
#         x = torch.flatten(x, 1)
#
#         # 动态初始化全连接层
#         if self.fc1 is None:
#             self.fc1 = nn.Linear(x.shape[1], 128).to(x.device)
#
#         x = F.relu(self.fc1(x))
#         x = self.fc2(x)
#         return x
#
# # 3️⃣ 训练设置
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# model = CNN().to(device)
# optimizer = optim.Adam(model.parameters(), lr=0.001)
# criterion = nn.CrossEntropyLoss()
#
# train_losses = []
# test_losses = []
#
# # 4️⃣ 训练与验证
# for epoch in range(3):
#     model.train()
#     running_loss = 0
#     for data, target in train_loader:
#         data, target = data.to(device), target.to(device)
#         optimizer.zero_grad()
#         output = model(data)
#         loss = criterion(output, target)
#         loss.backward()
#         optimizer.step()
#         running_loss += loss.item()
#     train_losses.append(running_loss / len(train_loader))
#
#     # 测试
#     model.eval()
#     test_loss = 0
#     correct = 0
#     with torch.no_grad():
#         for data, target in test_loader:
#             data, target = data.to(device), target.to(device)
#             output = model(data)
#             test_loss += criterion(output, target).item()
#             pred = output.argmax(dim=1)
#             correct += pred.eq(target).sum().item()
#     test_loss /= len(test_loader)
#     acc = 100. * correct / len(test_loader.dataset)
#     test_losses.append(test_loss)
#     print(f"Epoch {epoch+1}: Train Loss = {train_losses[-1]:.4f}, Test Loss = {test_loss:.4f}, Accuracy = {acc:.2f}%")
#
# # 5️⃣ 可视化训练过程
# plt.figure(figsize=(8, 4))
# plt.plot(train_losses, label="Train Loss")
# plt.plot(test_losses, label="Test Loss")
# plt.xlabel("Epoch")
# plt.ylabel("Loss")
# plt.legend()
# plt.show()
#
# # 6️⃣ 显示预测结果
# examples = enumerate(test_loader)
# batch_idx, (example_data, example_targets) = next(examples)
# with torch.no_grad():
#     output = model(example_data.to(device))
# pred = output.argmax(dim=1)
#
# plt.figure(figsize=(12, 5))
# for i in range(10):
#     plt.subplot(2, 5, i + 1)
#     plt.imshow(example_data[i][0], cmap='gray')
#     plt.title(f"Pred: {pred[i].item()}")
#     plt.axis("off")
# plt.show()



import torch
from tensorflow.python.ops.linalg.sparse.sparse_csr_matrix_ops import matmul

dtype = torch.float
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

a = torch.randn(2,3,device = device,dtype = dtype)#创建一个2*3的随机张量
b = torch.randn(2,3,device = device,dtype = dtype)#再创建一个2*3的随机张量
print("a张量：")
print(a)
print("b张量：")
print(b)

print(a*b)#a和b逐元素相乘

#输出张量a的所有元素之和
print("a张量的所有元素之和为：")
print(a.sum())

#输出张量a中第2行第3列的元素
print('张量a中第2行第3列的元素:')
print(a[1,2])

#输出张量a中的最大值
print('张量a中的最大值:')
print(a.max())

# 创建一个 2x3 的全 0 张量
a = torch.zeros(2,3)
print(a)

# 创建一个 2x3 的全 1 张量
b = torch.ones(2,3)
print(b)

# 从 NumPy 数组创建张量
import numpy as np
numpy_array = np.array([[1,2],[3,4]])
tensor_from_numpy = torch.from_numpy(numpy_array)
print(numpy_array)
print(tensor_from_numpy)

e = torch.randn(2,3)
f = torch.randn(2,3)
print('e:',e)
print('f:',f)
print(e + f)
print(e - f)
print(e * f)
print(e.t())
print(e.shape)

# 创建一个需要梯度的张量
tensor_requires_grad = torch.tensor([1.0],requires_grad=True)
print('tensor_requires_grad:',tensor_requires_grad)
#进行一些操作
tensor_result = tensor_requires_grad * 2
tensor_result.backward()
print('tensor_requires_grad.grad:',tensor_requires_grad.grad)


#创建一个需要计算梯度的向量
x = torch.randn(2,2,requires_grad=True)
print('x:',x)
y = x+2
print('y:',y)
z = y*y*3
print('z:',z)
out = z.mean()
out.backward()
print('out:',out)
print(1.5 * (x+2))
print('x.grad:',x.grad)



d = torch.tensor([[1,2,3],[4,5,6]],dtype=torch.float32)    #2*3
print('原始张量d:',d)
#1.索引和切片
print("获取第一行：",d[0,])
print("获取第一行：",d[0])
print('获取第一行第一列的元素：',d[0,0])
print('获取第二列的所有元素:',d[:,1])

reshape = d.view(3,2)
reshape2 = d.reshape(3,2)
print('改变张量形状为3*2：',reshape)
print('改变张量形状为3*2：',reshape2)
flatten = d.flatten()
print('展平后的张量：',flatten)

d2 = torch.tensor([[1,1,1],[2,2,2]],dtype=torch.float32)
m = torch.matmul(d,d2.t())
print('两个张量的乘积：',m)

#条件筛选与判断
mask = d > 3  #创建一个布尔掩码
print('大于3的元素的布尔掩码：',mask)
filtered_d = d[d>3]
print('大于3的元素:',filtered_d)
