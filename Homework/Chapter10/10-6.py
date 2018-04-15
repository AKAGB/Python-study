try:
    a = input('Number 1: ')
    b = input('Number 2: ')
    print(int(a) + int(b))
except ValueError:
    print('Please input a number.')