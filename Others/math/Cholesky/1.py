import numpy as np
from apis import *

while True:
    order = input('请输入n (Hilbert矩阵的阶数)或"q!"以退出: ')
    if order == 'q!':
        break
    n = int(order)
    dis = input('是否发生扰动(y/n)：')

    Hn = Hilbert(n)                # Hilbert矩阵
    x = np.ones(n)                 # 各分量均为1的x
    b = generateB(Hn.copy())        # 获得b
    if dis == 'y':
        b += 1e-7                   # 添加扰动
    x_s = cho_solute(Hn, b)         # 近似解x

    b = generateB(Hn.copy())        # 计算残差r时确保b是无扰动的
    r = b - np.dot(Hn, x_s)         # 残差r
    deltaX = x_s - x                # x的误差
    print('\n||r|| = %g, ||delatX|| = %g.\n' % (infinite_norm(r), infinite_norm(deltaX)))