import numpy as np
import torch
from torch.utils.data import TensorDataset,DataLoader
import torch.nn as nn
import torch.optim as optim
from  sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from torchsummary import summary


def creat_dataset():
    data = pd.read_csv('data/手机价格预测.csv')
    x = data.iloc[:,:-1].values.astype(np.float32)     #[,],左边为行,右边为列,:-1表示到最后一行的前一行,-1表示选取最后一列（负索引从-1开始，-1即最后一列）。,包左不包右,即所有行和除了最后一列的其他所有列
    y = data.iloc[:,-1].values.astype(np.int64)
    #划分训练集
    x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.8)
    train_dataset = TensorDataset(torch.tensor(x_train),torch.tensor(y_train))
    test_dataset = TensorDataset(torch.tensor(x_test),torch.tensor(y_test))
    return train_dataset,test_dataset,x_train.shape[1],len(np.unique(y))

# train_dataset,test_dataset,input_dim,class_num =creat_dataset()
# print(input_dim)
# print(class_num)
class Model(nn.Module):
    def __init__(self):
        super(Model,self).__init__()
        self.l1 = nn.Linear(20,128)
        self.l2 = nn.Linear(128,256)
        self.out = nn.Linear(256,4)

    def forward(self,x):
            x = torch.relu(self.l1(x))
            x = torch.relu(self.l2(x))
            out = self.out(x)
            return out

net = Model()
summary(net,input_size=(20,),batch_size=16)