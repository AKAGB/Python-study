import json

num = input('Input the number you like: ')
with open('data.json', 'w') as f:
    json.dump(int(num), f)
