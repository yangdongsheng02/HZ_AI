# n = 10
# squares_list = []
# squares_set = set()
# squares_list = [i**2 for i in range(1, n + 1)]
# print(squares_list)
# squares_set = set(squares_list)
# print(squares_set)

# 定义要生成的平方数的数量
n = 10
# 使用列表推导式生成平方数列表
squares_list = [i**2 for i in range(1, n + 1)]
# 将列表转换为集合
squares_set = set(squares_list)
# 输出结果
print("平方数集合:", squares_set)



names = ['Alice', 'Bob', 'Charlie']
# 定义年龄列表
ages = [25, 30, 35]
people_dict = {names[i] : ages[i] for i in range(len(names))} #[i]为索引下标
print("\n名字列表:", names)
print("年龄列表:", ages)
print("拼接后的字典:", people_dict)
# 1. 循环部分：for i in range(len(names))
# len(names) = 3
# range(3) → [0, 1, 2]
# 循环3次：i = 0, 1, 2
# 2. 键值对部分：names[i] : ages[i]
# 第1次循环 (i=0): names[0] : ages[0] → 'Alice' : 25
# 第2次循环 (i=1): names[1] : ages[1] → 'Bob' : 30
# 第3次循环 (i=2): names[2] : ages[2] → 'Charlie' : 35