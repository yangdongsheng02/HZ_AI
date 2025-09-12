import torch

# data = torch.tensor([[1,2,3],[4,5,6]])
# print(data.shape)      #shape属性获得张量形状
# print(data.size())      #size()方法获得张量形状
#
# print(data.reshape(1, 6).shape)    #reshape()修改张量形状
# print(data.reshape(3, -1).shape)      #用-1会自动计算取合适的值来取代这里的-1

# data = torch.tensor([1,2,3,4,5])
# print(data.shape)
# print (data)
# data2 = data.double()
# print(data.unsqueeze(0).shape)
# print(data.unsqueeze(0).squeeze().shape)

data = torch.Tensor(2,3)
print(data.shape)
print(data.is_contiguous())
data = data.contiguous()    #view只能用于连续的张量,如果不连续可以用contiguous()转换为连续的
print = (data.view(3,2).shape)
