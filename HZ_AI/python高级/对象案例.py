# class Student:
#     def __init__(self):
#         self.weight = 100
#
#     def run(self):
#         self.weight -= 0.5
#         print(f'跑步一次之后体重为{self.weight}')
#
#     def eat(self):
#         self.weight += 0.5
#         print(f'大吃大喝后体重为{self.weight}')
#
# xiaoming = Student()
# xiaoming.run()
# xiaoming.eat()

#烤地瓜
class SweetPotato:
    #初始化属性
    def __init__(self):
        self.cook_time = 0
        self.cook_state = '生的'
        self.condi_list = []

    #地瓜被烤
    def cook(self,time):
        #被烤时间
        self.cook_time += time
        if 0<=self.cook_time<3:
            self.cook_state = '生的'
        elif 3<=self.cook_time<7:
            self.cook_time = '半生不熟'
        elif 7<=self.cook_time<12:
            self.cook_time = '熟了'
        else:
            self.cook_time = '已烤焦，糊了'

    #添加调料
    def add_condi(self,condi):
        self.condi_list.append(condi)

    #信息输出
    def __str__(self):
        return f'这个地瓜烤了{self.cook_time},状态是{self.cook_state},添加了{self.condi_list}'

#创建对象
potato = SweetPotato()
print(potato)

#调用方法
potato.cook(3)
potato.add_condi('蜂蜜')
print(potato)

