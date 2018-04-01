import re
while True:
    input_str = input('请输入您的年龄(输入 q! 以退出)：')
    if input_str == 'q!':
        break
    if re.match(r'^\d+$', input_str):
        age = int(input_str)
        if age < 3:
            print('您可以免费入场。')
        elif age <= 12:
            print('您的票价为10美元。')
        else:
            print('您的票价为15美元。')
    else:
        print('输入不合法，请重新输入。')