names = ['Sam', 'Alice', 'Tom', 'Bob', 'Kitty']
print('Names:', names)

while len(names) > 2:
    name = names.pop()
    print(name + ', I\'m sorry to tell you I cannot invite you to my party.')

print(names[0] + ', I\'m glad to tell you that you are still invited.')
print(names[1] + ', I\'m glad to tell you that you are still invited.')
del names[0]
del names[0]
print('Names:', names)