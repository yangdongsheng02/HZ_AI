import torch

data = torch.randint(0,10,[4,5])
print(data)

# print(data[0,:])
# print(data[:,0])
# print(data[1,2])
#
#
# print(data[[0,1],[1,2]])    #[0]行的[1]个元素和[1]行[2]列元素
print(data[[[0],[1]],[1,2]])    #第[0]行和第[1]行的第[1]列和第[2]列元素
