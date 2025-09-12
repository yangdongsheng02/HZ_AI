def greet(name):
    print(f'{name},您好')
greet('鹏鹏')

def return_num():
    return 1, 2


result = return_num()
print(result)
print(type(result))  # <class 'tuple'>

def size(num1, num2):
    jia = num1 + num2
    jian = num1 - num2
    cheng = num1 * num2
    chu = num1 / num2
    return jia, jian, cheng, chu
print(size(20,5))

def calculate_sum(numbers_list):
    even_sum = 0 #ji shu he
    odd_sum = 0  #偶数和
    for num in numbers_list:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return [even_sum, odd_sum]
numbers = [2, 5, 3, 7, 5, 7]
result = calculate_sum(numbers)
print(f'偶数和为{result[0]},奇数和为{result[1]}')


def func(*args, **kwargs):
    print(args)
    print(kwargs)


# 定义一个元组（也可以是列表）
tuple1 = (10, 20, 30)
# 定义一个字典
dict1 = {'first': 40, 'second': 50, 'third': 60}
# 需求：把元组传递给*args参数，字典传递给**kwargs
# ① 如果想把元组传递给*args，必须在tuple1的前面加一个*号
# ② 如果想把字典传递给**kwargs，必须在dict1的前面加两个**号
func(*tuple1, **dict1)