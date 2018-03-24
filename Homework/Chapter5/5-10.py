current_users = ['mike', 'john', 'sam', 'tony', 'ben']
new_users = ['Jack', 'Tom', 'Tony', 'Sarah', 'John']

for user in new_users:
    if user.lower() in current_users:
        print('Please input other user name.')
    else:
        print('"' + user + '" isn\'t used.')