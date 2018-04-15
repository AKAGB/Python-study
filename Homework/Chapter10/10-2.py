with open('learning_python.txt') as f:
    for i in f:
        print(i.replace('Python', 'C').strip())