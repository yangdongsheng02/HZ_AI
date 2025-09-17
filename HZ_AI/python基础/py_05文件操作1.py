import os
if not os.path.exists('../../images'):
    os.mkdir('../../images')

if not os.path.exists('images/avatar'):
    os.mkdir('images/avatar')

print(os.getcwd())

os.chdir('images/avatar')
print(os.getcwd())

os.chdir('../../../../')
print(os.getcwd())

print(os.listdir())
os.rmdir('images/avatar')