try:
    print(name)
except Exception as e:
    print(e)

try:
    f = open('python.txt', 'r')
except:
    f = open('python.txt', 'w')
else:
    content = f.readlines()
    print(content)
finally:
    f.close()