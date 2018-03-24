lst = [x for x in range(1,10)]
for each in lst:
    if each == 1:
        print('1st')
    elif each == 2:
        print('2nd')
    elif each == 3:
        print('3rd')
    else:
        print('%dth' % each)