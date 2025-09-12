import torch

data = torch.randint(0,10,[2,3],dtype=torch.float64)

print(data)
print(data.mean)
print(data.sum())
print(torch.pow(data, 2)) #幂运算
print(data.sqrt_())        #平方根
print(data.exp())           #e^n次方
print(data.log())          #以e为底
print(data.log2())
print(data.log10())
