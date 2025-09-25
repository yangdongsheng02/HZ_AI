# 1,定义类
class Car:
    # 1.1 属性的设置
    def __init__(self):
        self.color = '红色'
        self.number = 4

    # 1.2 str:输出属性信息
    def __str__(self):
        # return f'{self.color}的汽车有{self.number}个车轮'
        return(f'{self.color}的汽车有{self.number}个车轮')



# 2.创建对象
car = Car()

# 3.打印对象
print(car)
