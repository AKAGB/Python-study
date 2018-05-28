import numpy as np
import matplotlib.pyplot as plt

def getA(t, fs):
    """t为自变量，fs为基函数列表"""
    A = np.array(list(map(fs[0], t)))
    for f in fs[1:]:
        A = np.vstack((A, np.array(list(map(f, t)))))
    return A.transpose()

def leastSq(x, y, fs):
    """线性最小二乘，x为自变量列表，y为因变量列表，fs为基函数"""
    A = getA(x, fs)
    C = np.dot(A.transpose(), A)
    b = np.dot(A.transpose(), y)
    x = np.linalg.solve(C, b)
    return x

def epsi(y, y_):
    """计算残差"""
    result = 0
    for i, j in zip(y, y_):
        result += (i - j)**2
    result /= len(y)
    return result**0.5

def getS(coms, fs, x):
    """返回拟合函数带入x的值"""
    result = 0
    l = len(coms)
    for i in range(l):
        result += coms[i] * fs[i](x)
    return result

if __name__ == '__main__':
    x = np.array([0, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    y = np.array([1, 1.75, 1.96, 2.19, 2.44, 2.71, 3.00])

    # 利用最小二乘法，拟合的多项式为 y = kx + b
    fai1 = lambda x : 1
    fai2 = lambda x : x
    fs = [fai1, fai2]
    # coms = [k, b]
    coms = leastSq(x, y, fs)

    # 拟合后的y
    y_ = [getS(coms, fs, i) for i in x]
    print('e =', epsi(y, y_))
    plt.scatter(x, y, color='r')
    plt.plot(x, y_, color='b')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    