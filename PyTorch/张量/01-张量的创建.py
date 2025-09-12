import torch
import numpy as np
# # 1. 创建张量标量
# data = torch.tensor(10)
# print(data)
# # 2. numpy 数组, 由于 data 为 float64, 下面代码也使用该类型
# data = np.random.randn(2, 3)
# data = torch.tensor(data)
# print(data)
# # 3. 列表, 下面代码使用默认元素类型 float32
# data = [[10., 20., 30.], [40., 50., 60.]]
# data = torch.tensor(data)
# print(data)

# data = torch.zeros(2,3)
# print(data)
# data = torch.ones(2,3)
# print(data)
#
# data = torch.full([2,3],10)
# print(data)
#
# print(torch.full([2, 3], 5))

data = torch.full((2,3), 6)
print(data.dtype)
data1=data.type(torch.DoubleTensor)
print(data1.dtype)

data2 = data.double()
print(data2.dtype)