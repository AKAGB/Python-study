import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as LA

from math import e
from math import log
from ex1 import *

def p(y):
    """返回y次函数"""
    return lambda x : x**y

def ln_cond(x, n):
    fs = [p(x) for x in range(n+1)]
    A = getA(x, fs)
    return log(LA.cond(A))

def ep(x, y, n):
    # 生成基函数
    fs = [p(x) for x in range(n+1)]
    coms = leastSq(x, y, fs)
    # 用于计算残差  
    y_1 = [getS(coms, fs, i) for i in x]
    return epsi(y_1, y)

if __name__ == '__main__':
    
    # 生成数据
    x = np.linspace(-1, 1, 20)
    y = np.array(list(map(lambda x : e**x, x)))

    ns = [3, 5, 7, 9]
    ls = [ln_cond(x, i) for i in ns]
    eps = [ep(x, y, i) for i in ns]
    for i in range(len(ns)):
        print('σ(%d) = %g' % (ns[i], eps[i]))
    # plt.scatter(x, y)
    plt.plot(ns, ls, label='p1')
    plt.xlabel('n')
    plt.ylabel('ln(cond(A))')
    plt.show()