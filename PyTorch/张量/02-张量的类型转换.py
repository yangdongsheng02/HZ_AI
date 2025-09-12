import torch
import numpy as np

# #张量转数组
# data = torch.tensor([2,3,4])
# data_numpy = data.numpy()
# print(type(data))
# print(type(data_numpy))

#NumPy数组转换为张量
# data = np.array([2,3,4])
# print(type(data))
# print(type(torch.from_numpy(data)))
# print(type(torch.tensor(data)))
#

##点乘
# data1 = torch.tensor([[1,2],[3,4]])
# data2 = torch.tensor([[5,6],[7,8]])
# print(torch.mul(data1,data2))
# print(data1*data2)

##数组乘法(矩阵乘法)
data1 = torch.tensor([[1,2],[3,4],[5,6]])
data2 = torch.tensor([[5,6],[7,8]])
print(data1@data2)
print(torch.matmul(data1,data2))