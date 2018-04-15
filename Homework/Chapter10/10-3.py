name = input('Please input your name: ')
with open('guest.txt', 'w') as f:
    f.write(name + '\n')