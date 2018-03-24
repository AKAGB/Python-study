dog = {
    'type': 'dog',
    'master': 'Tom'
}
cat = {
    'type': 'cat',
    'master': 'Sam'
}
turtle = {
    'type': 'turtle',
    'master': 'Sarah'
}
pets = [dog, cat, turtle]

for pet in pets:
    print('Pet type: ' + pet['type'])
    print('Pet\'s master: ' + pet['master'] + '\n')