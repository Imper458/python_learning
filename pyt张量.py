import torch
import numpy as np
#创建张量
x = torch.tensor([[1,2],[3,4]])
x = torch.zeros(2,3)#全为0
x = torch.ones(2,3)#全为1
x = torch.empty(2,3)#空
x = torch.rand(2,3)#均匀分布【0，1】
x = torch.randn(2,3)#标准正太分布
x = torch.arange(0,10,2)#创建一个一维序列张量，从0到10（10取不到），步长为2
print(x)
x = torch.linspace(0,6,6)#创建一个从0到5的序列张量，等间隔取6个数
print(x)
x = torch.eye(3)#创建3维的单位矩阵
print(x)
x = torch.from_numpy(np.array([[1,2],[3,4]]))
print(x)

tensor_2d = torch.tensor([
    [-9, 4, 2, 5, 7],
    [3, 0, 12, 8, 6],
    [1, 23, -6, 45, 2],
    [22, 3, -1, 72, 6]
])
print("2D Tensor (Matrix):\n", tensor_2d)
print("Shape:", tensor_2d.shape)  # 形状

# 创建 3D 张量（立方体）
tensor_3d = torch.stack([tensor_2d, tensor_2d + 10, tensor_2d - 5])  # 堆叠 3 个 2D 张量
print("3D Tensor (Cube):\n", tensor_3d)
print("Shape:", tensor_3d.shape)  # 形状
print("Size:", tensor_3d.size())
print("dim:", tensor_3d.dim())
print("device:", tensor_3d.device)
print("grad:", tensor_3d.requires_grad)
print("numel:", tensor_3d.numel())
print("cuda:", tensor_3d.is_cuda)
print("转置:",tensor_2d.T)
print("item:",tensor_3d[0,0,0].item())
print("contiguous:", tensor_3d.is_contiguous())
'''
获取张量的形状：tensor.shape
获取张量的形状：tensor.size()
获取张量的数据类型：tensor.dtype
查看张量所在的设备 (CPU/GPU)：tensor.device
获取张量的维度数：tensor.dim
是否启用梯度计算：tensor.requires_grad
获取张量中的元素总数：tensor.numel()
检查张量是否在 GPU 上：tensor.is_cuda
获取张量的转置（适用于 2D 张量）：tensor.T
获取单元素张量的值：tensor.item()
检查张量是否连续存储：tensor.is_contiguous()

'''

#张量的操作
'''
元素级加法、减法、乘法、除法：+-*/
矩阵乘法：z = torch.matmul(x,y)
向量点积（仅适用于 1D 张量）：	z = torch.dot(x, y)
求和：	z = torch.sum(x)
求均值：	z = torch.mean(x)
求最大值：	z = torch.max(x)
求最小值：	z = torch.min(x)
返回最大值的索引（指定维度）：	z = torch.argmax(x, dim=1)
计算 softmax（指定维度）：	z = torch.softmax(x, dim=1)
'''
#形状的操作
'''
x.view(shape)	改变张量的形状（不改变数据）。	z = x.view(3, 4)
x.reshape(shape)	类似于 view，但更灵活。	z = x.reshape(3, 4)
x.t()	转置矩阵。	z = x.t()
x.unsqueeze(dim)	在指定维度添加一个维度。	z = x.unsqueeze(0)
x.squeeze(dim)	去掉指定维度为 1 的维度。	z = x.squeeze(0)
torch.cat((x, y), dim)	按指定维度连接多个张量。	z = torch.cat((x, y), dim=1)
'''
a = torch.tensor([[1,2],[3,4]])
print('a:',a)
print(a.unsqueeze(0))
print(a.squeeze(0))
print('a的形状是：',a.shape)