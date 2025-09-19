# str = "banana and apple"
# count = 0
# for i in str:
#     if i == 'a':
#         count += 1
# print(count)

# str = 'Python is a great programming language'
# count = 0
# for i in str:
#     if i == ' ':
#         count += 1
# print(count)

# str = '"我认为人工智能必然是未来的方向。人工智能将改变世界。人工智能很重要"'
# print(str.find('人工智能'))
# email = 'username@example.com'
# i = email.find('@')
# print(f'用户名为{email[:i:]}')
# print(f'域名为{email[i+1::]}')

# for i in str:
#     if str.find('人工智能') != -1:
#         a = (str.find('人工智能'))
#         print(a)
#         a += 1


# start = 0
# while  True:
#     index = str.find('人工智能',start)
#     if index == -1:
#         break
#     print(index)
#     start = index + 1

# str = '你大爷的,你到底会不会玩'
# print(str.replace('你大爷', '***'))
# date = '2025-09-19'
# print(date.split('-'))
# list = ['orange','juice']
# print('_'.join(list))
# list_num = [1,2,3,4,5,6]
# print(list_num[-3:])
#
# score = [1,2,3,4,5,6]
# sum = 0
# for i in score:
#     sum += i
# print(sum)
# print(len(score))

# list1 = ['刘备','关羽','张飞','赵云','诸葛亮','关羽']
# print(list1.index('关羽'))
# list2 = ['A','B','A','C','B','A','A','D']
# print(list2.count('A'))
# list3 = ['admin','root']
# user = input('输入用户名')
# if user in list3:
#     print('在权限列表中,欢迎登陆')
# else:
#     print("不在里面,普通用户登录")
# user1 = input('输入用户名')
# list4 = ['admin','bob','charlie']
# if user1 not in list4:
#     print("不在用户列表中,此用户名可用,注册成功")
# else:
#     print('用户名重复')


list = ['张明','小丽','小刘']
list.append('小美')
print(list)
list1 = ['董事长','民工1','民工2']
list1.insert(1,'儿子')
print(list1)
class1 = ['小明','小红','小刚']
class2 = ['小丽','小强','小华']
class3 = ['小张','小李','小王']
class4 = []
class4.extend(class1)
class4.extend(class2)
class4.extend(class3)
print(class4)


