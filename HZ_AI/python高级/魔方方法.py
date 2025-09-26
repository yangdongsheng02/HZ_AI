class Car:
    def __init__(self,color,number):
        #设置属性 __int__
        self.color = color
        self.number = number

        #获取属性:self.属性名
    def show(self):
        print(self.color)
        print(self.number)

    #del魔法
    def __del__(self):
        print('自动调用了del魔法方法')

    def __str__(self):
        print(f'{self.color}的汽车有{self.number}个车轮')

#创建对象:对象名 = 类名()
car = Car('红色',4)

# del car #删除对象,文件结束时也会调用
print(car.color)
print(car.number)
print(car.show())
print(car)