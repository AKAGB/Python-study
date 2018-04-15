import json

with open('data.json') as f:
    num = json.load(f)
print('I know your favorite number! It\'s %d.' % num)