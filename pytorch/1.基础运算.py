from cmath import exp

import torch
from torch.distributed.tensor import empty

#pytorch 张量基础操作
#1.创建一个未初始化的张量
x = torch.empty(5,3)
print("Empty Tensor:",x)

#2.创建一个随机初始化的张量
x = torch.rand(5,3)
print("Random Tensor:\n",x)

