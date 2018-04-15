# First
print('First:')
f = open('learning_python.txt', 'r')
text = f.read()
print(text)
f.close()

# Second
print('Second:')
f = open('learning_python.txt', 'r')
for eachline in f:
    print(eachline.strip())
f.close()

# Third
print('Third:')
with open('learning_python.txt') as f:
    lst = f.readlines()
for i in lst:
    print(i.strip())