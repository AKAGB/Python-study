names = ['Sam', 'Alice', 'Tom', 'Bob']
print('Names:', names)
names.insert(0, 'Guest1')
print('Names:', names)
names.insert(len(names) // 2, 'Guest2')
print('Names:', names)
names.append('Guest3')
print('Names:', names)