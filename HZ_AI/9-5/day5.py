import os
os.chdir('static')
print(os.getcwd())
if not os.path.exists('image'):
    os.mkdir('image')

print(os.listdir())
for file in os.listdir():
    print(file)
os.rmdir('test')

with open('./data/a.txt', 'rb') as src_f, open('./data/b.txt', 'wb') as dest_f:
    while True:
        data = src_f.read(8192)
        if len(data) <= 0:
            break
            dest_f.write(data)