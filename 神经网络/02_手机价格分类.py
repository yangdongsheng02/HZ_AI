import torch
from torch.utils.data import TensorDataset,DataLoader
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from torchsummary import summary



def creat_dataset():
    data = pd.read_csv('data/手机价格预测.csv')
    x = data.iloc[:,:-1].values.astype(np.float32)    # 特征矩阵：所有行 + 除最后一列外的所有列（float32） #[,],左边为行,右边为列,:-1表示到最后一行的前一行,-1表示选取最后一列（负索引从-1开始，-1即最后一列）。,包左不包右,即所有行和除了最后一列的其他所有列
    y = data.iloc[:,-1].values.astype(np.int64)      # 标签向量：所有行 + 最后一列（int64）
    #划分训练集
    x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.8)
    train_dataset = TensorDataset(torch.tensor(x_train),torch.tensor(y_train))# 训练集封装为TensorDataset
    test_dataset = TensorDataset(torch.tensor(x_test),torch.tensor(y_test))
    return train_dataset,test_dataset,x_train.shape[1],len(np.unique(y))# 返回数据集、输入维度、类别数


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

# net = Model()
# summary(net,input_size=(20,),batch_size=16)


#模型训练
def train(dataset):
    model = Model()         #模型的实例化
    loss = nn.CrossEntropyLoss() # 交叉熵损失函数（适用于分类任务）
    optimizer =optim.SGD(model.parameters(),lr=0.001)  #随机梯度下降优化器,学习率0.001,model.parameters()优化的是模型的参数
    epochs = 50    #训练50个轮次
    for epoch in range(epochs): #遍历每个轮次
       dataloader = DataLoader(dataset,batch_size=8,shuffle=True)# 创建数据加载器（打乱数据+分批),获取数据
       #统计损失函数变化  total_loss ,total_num
       total_loss = 0   #用于累加所有批次的损失值
       total_num = 1    # 避免除零错误 #用于统计处理的批次数量
       for x,y in dataloader: #遍历每个batch_size的特征和目标值
            predict = model(x)# 前向传播计算预测值,model()会调用model方法中的foward方法,就是进行前向传播
            loss_value = loss(predict,y) #把预测结果predict和真实值y送进去计算损失值
            optimizer.zero_grad() #对梯度清零防止梯度累加影响下一次循环
            loss_value.backward() # 反向传播计算梯度
            optimizer.step() #更新模型参数
            total_loss += loss_value.item()
            total_num += 1
       print(epoch+1,total_loss/total_num)
    torch.save(model.state_dict(),'data/phone.pth')
# train_data,test_dataset,_,_ = creat_dataset()
# train(dataset = train_data)

#测试模型
def my_test(dataset):
    model = Model()     #初始化神经网络模型
    weights = torch.load('data/phone.pth')  #加载训练好的参数
    model.load_state_dict(weights)  #将参数注入模型
    correct = 0    #正确预测计数
    dataloader = DataLoader(dataset,batch_size=8,shuffle=False) #测试集加载器(不打乱
    for x,y in dataloader:
        output = model(x)   #向前传播计算预测值
        y_pred = torch.argmax(output,dim=1) #取概率最大的类别作为预测结果
        correct += (y_pred == y).sum()  #统计预测正确的样本数
    print(correct/len(dataset))     #计算并打印准确率

_,test_dataset,_,_ = creat_dataset()
my_test(test_dataset)

