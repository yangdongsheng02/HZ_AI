import time
from time import sleep

# 返回：格林制时间到当前时间的秒数
start = time.time()

# 编写一个循环
list1 = []
for i in range(1000000):
    list1.append(i)

end = time.time()
print(f'以上代码共执行了{end - start}s')

start1 = time.time()
sleep(3)
end1 = time.time()
print(end1 - start1)