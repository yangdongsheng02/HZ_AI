class Person():
    # 定义一个方法
    def speak(self):
        print(self)              # 打印self（实例对象本身）
        print('Nice to meet you!')

# 类的实例化（生成对象）
p1 = Person()
print(p1)        # 打印p1对象的内存地址
p1.speak()       # 调用speak方法，方法内会打印self

p2 = Person()
print(p2)        # 打印p2对象的内存地址
p2.speak()       # 调用speak方法，方法内会打印self