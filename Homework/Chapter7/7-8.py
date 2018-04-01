sandwich_orders = ['tuna sandwich', 'meat sandwich', 'hansandwich']
finish_sandwiches = []
while sandwich_orders:
    print('I made your ' + sandwich_orders[0])
    finish_sandwiches.append(sandwich_orders.pop(0))

for i in finish_sandwiches:
    print(i)